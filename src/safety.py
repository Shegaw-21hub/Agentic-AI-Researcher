import re

def validate_input(query: str) -> bool:
    """Task 4: Input validation for malicious or malformed queries."""
    forbidden_patterns = [r"ignore instructions", r"system override", r"delete", r"kill"]
    for pattern in forbidden_patterns:
        if re.search(pattern, query, re.IGNORECASE):
            return False
    return len(query.strip()) > 3  # Ensure query isn't empty or too short

def sanitize_output(text: str) -> str:
    """Task 4: Block or sanitize unsafe outputs."""
    # Simple example: Redact specific sensitive keywords if they appear
    sensitive_info = ["INTERNAL_SYSTEM_KEY", "USER_PASSWORD_123"]
    for word in sensitive_info:
        text = text.replace(word, "[REDACTED]")
    return text