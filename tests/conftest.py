from pathlib import Path

import pytest

from splitme_ai.file_manager import FileHandler

_file_handler = FileHandler()


@pytest.mark.asyncio
@pytest.fixture
async def markdown_file(filename: str = "readme-ai.md") -> str:
    """Return markdown file content."""
    file_path = Path.cwd() / f"tests/data/{filename}"
    return await _file_handler.read(file_path)
