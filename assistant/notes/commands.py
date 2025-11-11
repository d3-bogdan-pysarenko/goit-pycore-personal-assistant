"""
Implements all command functions for managing notes.

Functions might include:
- add_note()
- edit_note()
- delete_note()
- search_notes()
- show_all_notes()
- etc.

Responsibilities:
- Parse user arguments and call appropriate methods on Notebook.
- Return text responses for CLI output.
"""

from assistant.commands_enum import Command


def register_note_commands(commands):
    """Register commands in the main command dispatcher."""
    commands[Command.Notes.ADD_NOTE] = None
    commands[Command.Notes.EDIT_NOTE] = None
    commands[Command.Notes.DELETE_NOTE] = None
    commands[Command.Notes.SEARCH_NOTE] = None
    commands[Command.Notes.SHOW_NOTES] = None


def not_implemented(notebook, *args):
    """Not implemented command handler."""
    return f"Command '{args[0]}' is not implemented yet."