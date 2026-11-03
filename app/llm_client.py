import time

from google import genai
from langfuse import get_client

from app.config import GEMINI_API_KEY
from app.prompts import SYSTEM_PROMPT


client = genai.Client(api_key=GEMINI_API_KEY)

langfuse = get_client()


def generate_response(user_message: str) -> dict:

    prompt = f"""
{SYSTEM_PROMPT}

Customer message:
{user_message}

Provide the best possible customer support response.
"""

    max_retries = 3

    with langfuse.start_as_current_observation(
        name="customer_support_chatbot",
        as_type="generation",
        input=user_message,
        model="gemini-3.8-flash",
    ) as generation:

        for attempt in range(max_retries):

            try:

                start_time = time.time()

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt,
                )

                latency = time.time() - start_time

                generation.update(
                    output=response.text,
                    metadata={
                        "status": "success",
                        "latency_seconds": round(latency, 3),
                        "attempt": attempt + 1,
                    },
                )

                langfuse.flush()

                return {
                    "success": True,
                    "response": response.text,
                    "status": "success",
                    "latency_seconds": round(latency, 3),
                    "attempts": attempt + 1,
                    "trace_id": generation.trace_id,
                }

            except Exception as e:

                error_text = str(e)

                print(
                    f"\nAPI attempt {attempt + 1} failed:"
                )
                print(error_text)

                # Daily quota / rate-limit error
                if (
                    "429" in error_text
                    or "RESOURCE_EXHAUSTED" in error_text
                    or "quota" in error_text.lower()
                ):

                    error_message = (
                        "The AI service has reached its current "
                        "API quota. Please try again later."
                    )

                    generation.update(
                        output=error_message,
                        metadata={
                            "status": "quota_exceeded",
                            "attempts": attempt + 1,
                        },
                    )

                    langfuse.flush()

                    return {
                        "success": False,
                        "response": error_message,
                        "status": "quota_exceeded",
                        "error": error_text,
                        "attempts": attempt + 1,
                    }

                # Retry temporary API errors
                if attempt < max_retries - 1:

                    wait_time = 2 ** attempt

                    print(
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:

                    error_message = (
                        "Sorry, the AI service is temporarily "
                        "unavailable. Please try again later."
                    )

                    generation.update(
                        output=error_message,
                        metadata={
                            "status": "api_failure",
                            "attempts": max_retries,
                        },
                    )

                    langfuse.flush()

                    return {
                        "success": False,
                        "response": error_message,
                        "status": "api_failure",
                        "error": error_text,
                        "attempts": max_retries,
                    }