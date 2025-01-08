"""Utilities for sanitizing filenames from markdown headers."""

import html
import re
from pathlib import Path


def sanitize_filename(text: str, extension: str = ".md") -> Path:
    """
    Convert a markdown header into a safe filename.

    Args:
        text: The header text to sanitize
        extension: File extension to append (defaults to .md)

    Returns:
        Path object with sanitized filename
    """
    # Decode any HTML entities
    text = html.unescape(text)

    # Remove markdown heading markers
    text = re.sub(r"^#+\s*", "", text)

    # Remove image references and inline HTML
    # Handle markdown-style image references
    text = re.sub(r"!\[([^\]]*)\]\([^\)]*\)", r"\1", text)  # Inline images
    text = re.sub(r"!\[([^\]]*)\]\[[^\]]*\]", r"\1", text)  # Reference-style images

    # Remove inline HTML (e.g., `<img src=...>`)
    text = re.sub(r"<[^>]+>", "", text)

    # Remove markdown attributes in curly braces (e.g., `{ width="2%" }`)
    text = re.sub(r"\{[^}]*\}", "", text)

    # Remove markdown links
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)  # Inline links
    text = re.sub(r"\[([^\]]+)\]\[[^\]]+\]", r"\1", text)  # Reference-style links

    # Remove any remaining markdown syntax
    text = re.sub(r"[*_`~]", "", text)

    # Convert to lowercase, replace spaces and special characters with hyphens
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)  # Remove any remaining special characters
    text = re.sub(r"[-\s]+", "-", text)  # Replace spaces and repeated hyphens

    # Remove leading/trailing hyphens
    text = text.strip("-")

    # Ensure valid text
    if not text:
        text = "unnamed-section"

    # Limit filename length
    max_length = 255 - len(extension)
    if len(text) > max_length:
        text = text[:max_length]

    # Add extension and return as Path object
    return Path(f"{text}{extension}")


def strip_markdown_header(text: str) -> str:
    """Remove only the markdown header markers from text.

    Args:
        text: The header text containing markdown syntax

    Returns:
        Text with header markers removed but other formatting intact
    """
    return re.sub(r"^#+\s*", "", text)


def extract_image_alt_text(text: str) -> str:
    """Extract alt text from markdown image references.

    Args:
        text: Text containing markdown image references

    Returns:
        Extracted alt text or empty string if none found
    """
    match = re.search(r"!\[([^\]]*)\]", text)
    return match.group(1) if match else ""
