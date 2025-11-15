"""
Contains shared validation utilities for various input types.

Functions:
- validate_phone(): Checks phone number format.
- validate_email(): Validates email address format.
- Possibly other helpers for addresses or tags.

Responsibilities:
- Reusable validation logic used across modules.
"""
import re


def validate_email(email: str) -> bool:
    """Перевіряє правильність email адреси."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))
