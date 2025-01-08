from pathlib import Path
from typing import Any, Dict, Union

import aiofiles

from splitme_ai.file_handler.base import AbstractFileHandler
from splitme_ai.utils.module_checker import is_available


class TOMLFileHandler(AbstractFileHandler):
    """
    File handler for TOML files.
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
        """Reads the content of a TOML file."""
        if is_available("tomllib"):
            import tomllib

            async with aiofiles.open(file_path, mode="rb") as file:
                return tomllib.loads((await file.read()).decode())
        elif is_available("toml"):
            import toml

            async with aiofiles.open(file_path) as file:
                return toml.loads(await file.read())
        else:
            raise ImportError("No TOML library available in the current environment.")

    async def read(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        """Reads the content of a TOML file."""
        return await self._cache_read(str(file_path))

    async def write(self, file_path: Union[str, Path], content: Dict[str, Any]) -> None:
        """Writes the content to a TOML file."""
        if is_available("tomli-w"):
            import tomli_w

            async with aiofiles.open(file_path, mode="wb") as file:
                await file.write(tomli_w.dumps(content).encode("utf-8"))

        elif is_available("toml"):
            import toml

            async with aiofiles.open(file_path, mode="wb") as file:
                await file.write(toml.dumps(content).encode("utf-8"))
        else:
            raise ImportError("No TOML library available in the current environment.")

        # Invalidate cache on write
        file_path_str = str(file_path)
        if file_path_str in self.cache:
            del self.cache[file_path_str]
            self.lru.remove(file_path_str)
