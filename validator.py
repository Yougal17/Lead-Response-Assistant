def validate_response(text):
    """
    Checks if the response contains risky or overly certain language.
    Returns True if safe, False if risky.
    """

    forbidden_phrases = [
        "definitely",
        "guaranteed",
        "100% sure",
        "must be",
        "this is caused by",
        "the root cause is",
        "it will worsen",
        "you need to immediately"
    ]

    text_lower = text.lower()

    for phrase in forbidden_phrases:
        if phrase in text_lower:
            return False

    return True
