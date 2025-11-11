"""
Provides shared utilities for the command-line interface:
- The `input_error` decorator for unified exception handling.
- The `parse_input()` function for splitting user input into command and arguments.
- Optionally, a central command dispatcher function (if needed later).

Responsibilities:
- Contain only CLI parsing and error handling logic.
"""


def input_error(func):
    """Decorator to handle input errors."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format. Please provide all required arguments."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return inner


def parse_input(user_input):
    """Parse user input into command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
