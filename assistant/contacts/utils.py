"""
Helpers for the contacts module.

Currently provides utilities for formatting contact output blocks with icons
and alignment, so that CLI output looks consistent with other parts of the app.
"""

from __future__ import annotations

from typing import Iterable, Optional

from .record import Record


# Icons used across contact formatting
ICON_PERSON = "👤"
ICON_PHONE = "📞"
ICON_CAKE = "🎂"
ICON_LETTER = "✉️"
ICON_HOME = "🏠"


def _phones_str(record: Record) -> str:
    return "; ".join(p.value for p in record.phones) if record.phones else "no phone numbers"


def _birthday_str(record: Record) -> str:
    return record.birthday.value.strftime("%d.%m.%Y") if record.birthday else "not specified"


def _email_str(record: Record) -> str:
    return record.email.value if record.email else "not specified"


def _address_str(record: Record) -> str:
    return record.address.value if record.address else "not specified"


def format_contact(
    record: Record,
    include_fields: Optional[Iterable[str]] = None,
    *,
    birthday_override: Optional[str] = None,
) -> str:
    """
    Build a formatted, multi-line string for a contact using icons and a tabbed
    alignment on each data row.

    Example output:
    
    👤 John:
    	📞 Phones: 123; 456
    	🎂 Birthday: 01.01.1990
    	✉️ Email: john@example.com
    	🏠 Address: 221B Baker St

    Parameters
    - record: the contact to format
    - include_fields: optional iterable of field keys to include. Supported keys:
      {"phones", "birthday", "email", "address"}. If None, include all.
    - birthday_override: optional textual birthday value to display instead of
      the record's own birthday (useful for "upcoming birthdays" view).
    """

    all_fields = ["phones", "birthday", "email", "address"]
    fields = list(include_fields) if include_fields is not None else all_fields

    lines = [f"{ICON_PERSON} {record.name.value}:"]

    if "phones" in fields:
        lines.append(f"\t{ICON_PHONE} Phones: {_phones_str(record)}")
    if "birthday" in fields:
        bday = birthday_override if birthday_override is not None else _birthday_str(record)
        lines.append(f"\t{ICON_CAKE} Birthday: {bday}")
    if "email" in fields:
        lines.append(f"\t{ICON_LETTER} Email: {_email_str(record)}")
    if "address" in fields:
        lines.append(f"\t{ICON_HOME} Address: {_address_str(record)}")

    return "\n".join(lines)
