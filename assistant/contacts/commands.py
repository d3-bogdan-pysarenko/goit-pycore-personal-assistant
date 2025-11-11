"""
Implements all command functions related to contact management.

Functions:
- add_contact()
- change_contact()
- show_phone()
- show_all()
- add_birthday()
- show_birthday()
- birthdays()
- etc.

Responsibilities:
- Parse and validate command arguments.
- Interact with the AddressBook and Record classes.
- Return text messages to be printed by main.py.
"""

from assistant.commands_enum import Command


def register_contact_commands(commands):
    """Register commands in the main command dispatcher."""
    commands[Command.Contacts.ADD] = None
    commands[Command.Contacts.CHANGE] = None
    commands[Command.Contacts.PHONE] = None
    commands[Command.Contacts.ALL] = None
    commands[Command.Contacts.ADD_BIRTHDAY] = None
    commands[Command.Contacts.SHOW_BIRTHDAY] = None
    commands[Command.Contacts.BIRTHDAYS] = None
