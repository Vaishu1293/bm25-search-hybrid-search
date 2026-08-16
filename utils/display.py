"""Console display helpers."""

from config import AUTHOR, BANNER_WIDTH, PROJECT_NAME, VERSION


def display_banner() -> None:
    """Display the standard application header."""
    print("=" * BANNER_WIDTH)
    print(PROJECT_NAME)
    print(f"Version: {VERSION}")
    print(f"Author:  {AUTHOR}")
    print("=" * BANNER_WIDTH)


def display_startup_message() -> None:
    """Print the application startup message."""
    print("\nApplication Started Successfully\n")


def banner_workers() -> None:
    """Display the application banner and startup message."""
    display_banner()
    display_startup_message()