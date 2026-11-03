import os
from dotenv import load_dotenv
from langfuse import get_client


load_dotenv()


def main():
    public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
    secret_key = os.getenv("LANGFUSE_SECRET_KEY")
    base_url = os.getenv("LANGFUSE_BASE_URL")

    print("Langfuse configuration check:")
    print(
        "Public Key:",
        "FOUND" if public_key else "MISSING"
    )
    print(
        "Secret Key:",
        "FOUND" if secret_key else "MISSING"
    )
    print(
        "Base URL:",
        base_url if base_url else "MISSING"
    )

    if not public_key or not secret_key:
        print("\nLangfuse credentials are missing.")
        return

    langfuse = get_client()

    print("\nTesting Langfuse connection...")

    langfuse.create_event(
        name="connection_test"
    )

    langfuse.flush()

    print("Langfuse connection test completed successfully.")


if __name__ == "__main__":
    main()