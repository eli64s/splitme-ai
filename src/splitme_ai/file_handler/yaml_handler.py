from pathlib import Path
from typing import Any, Dict, Union

import aiofiles
import yaml

from splitme_ai.errors import FileWriteError
from splitme_ai.file_handler.base import AbstractFileHandler


class YAMLFileHandler(AbstractFileHandler):
    """
    File handler for YAML files.
    """

    def __init__(self, max_cache_size: int = 128) -> None:
        self.cache: Dict[str, Any] = {}
        self.max_cache_size = max_cache_size
        self.lru: list[str] = []

    async def _cache_read(self, file_path: str) -> Any:
        """Reads from cache or file, updating cache as needed."""
        if file_path in self.cache:
            self.lru.remove(file_path)
            self.lru.append(file_path)
            return self.cache[file_path]

        content = await self._read_from_file(file_path)

        if len(self.cache) >= self.max_cache_size:
            lru_item = self.lru.pop(0)
            del self.cache[lru_item]

        self.cache[file_path] = content
        self.lru.append(file_path)
        return content

    async def _read_from_file(self, file_path: str) -> Any:
        """Reads the content of a YAML file."""
        async with aiofiles.open(file_path, encoding="utf-8") as file:
            return yaml.safe_load(await file.read())

    async def read(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """Reads the content of a YAML file."""
        return await self._cache_read(str(file_path))

    async def write(self, file_path: Union[str, Path], content: Dict[str, Any]) -> None:
        """Writes the content to a YAML file."""
        file_path_ = str(file_path)
        try:
            async with aiofiles.open(file_path, mode="w", encoding="utf-8") as file:
                await file.write(
                    yaml.safe_dump(data=content, default_flow_style=False, indent=4)
                )
        except FileNotFoundError as e:
            raise FileWriteError(message="File not found", path=file_path_) from e
        except Exception as e:
            raise FileWriteError(
                message=f"Error writing file: {e}",
                path=file_path_,
            ) from e

        # Invalidate cache on write
        file_path_str = str(file_path)
        if file_path_str in self.cache:
            del self.cache[file_path_str]
            self.lru.remove(file_path_str)
