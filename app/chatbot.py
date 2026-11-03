from app.llm_client import generate_response
from app.validators import validate_response


def main():

    print("=" * 50)
    print("AI Customer Support Chatbot")
    print("=" * 50)

    user_input = input("\nYou: ")

    result = generate_response(user_input)

    # Check whether the LLM call was successful
    if not result["success"]:

        print("\nAI Assistant:", result["response"])

        print(
            f"\n[System Status] {result['status']}"
        )

        print(
            f"[API Attempts] {result['attempts']}"
        )

        return

    # Actual AI response
    response = result["response"]

    print("\nAI Assistant:", response)

    # Validate only genuine AI responses
    validation = validate_response(response)

    print("\n[Validation]")

    if validation["valid"]:

        print("Status : PASSED")
        print(f"Reason : {validation['reason']}")

    else:

        print("Status : FAILED")
        print(f"Reason : {validation['reason']}")


if __name__ == "__main__":
    main()