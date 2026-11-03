def validate_response(response: str) -> dict:
    """
    Validate the AI response for basic safety and quality checks.
    """

    if not response or not response.strip():
        return {
            "valid": False,
            "reason": "Empty response"
        }

    response_lower = response.lower()

    # These indicate that the model may have revealed sensitive information.
    sensitive_leak_patterns = [
        "my api key is",
        "the api key is",
        "here is your api key",
        "system prompt:",
        "here is the system prompt",
        "internal instructions are"
    ]

    for pattern in sensitive_leak_patterns:
        if pattern in response_lower:
            return {
                "valid": False,
                "reason": f"Potential sensitive information leak detected"
            }

    return {
        "valid": True,
        "reason": "Response passed validation"
    }