from pathlib import Path
from typing import Union

import aiofiles

from splitme_ai.file_handler.base import AbstractFileHandler


class TextFileHandler(AbstractFileHandler):
    """
    File handler for text-based files.
    """

    async def read(self, file_path: Union[str, Path]) -> str:
        """Reads the content of a text-based file (e.g., HTML, MD, TXT)."""
        async with aiofiles.open(file_path, encoding="utf-8") as file:
            return await file.read()

    async def write(self, file_path: Union[str, Path], content: str) -> None:
        """Writes the content to a text-based file (e.g., HTML, MD, TXT)."""
        async with aiofiles.open(file_path, mode="w", encoding="utf-8") as file:
            await file.write(content)
