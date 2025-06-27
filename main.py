# server.py
from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("AI Server")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


def ensure_file():
    """Ensure the notes file exists."""
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'w') as f:
            f.write("")

@mcp.tool()
def add_note(note: str) -> str:
    """
    Add a note to the notes file.

    Args:
        note (str): The note to add.
    Returns:
        str: Confirmation message.
    """
    ensure_file()
    with open(NOTES_FILE, 'a') as f:
        f.write(note + "\n")
    return f"Note added: {note}"


@mcp.tool()
def list_notes() -> str:
    """
    List all notes from the notes file.

    Returns:
        str: All notes as a string.
    """
    ensure_file()
    with open(NOTES_FILE, 'r') as f:
        notes = f.read().strip()
    return "".join(notes) if notes else "No notes found."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get latest note from the notes file.

    Returns:
        str: Latest note as a string.
    """
    ensure_file()
    with open(NOTES_FILE, 'r') as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes found."


@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a summary of the notes.

    Args:
        notes (str): The notes to summarize.
    Returns:
        str: Summary of the notes.
    """
    ensure_file()
    with open(NOTES_FILE, 'r') as f:
        notes = f.read().strip()
    if not notes:
        return "No notes to summarize."
    
    return f"Summary of notes: {notes}"