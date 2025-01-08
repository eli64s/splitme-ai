import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import aiofiles
import aiofiles.os

from splitme_ai.errors import FileReadError, FileWriteError
from splitme_ai.file_handler import get_handler
from splitme_ai.logger import Logger

_logger = Logger(__name__)


class FileHandler:
    """
    Handles file read/write operations, delegating to the appropriate file handler.
    """

    def __init__(self) -> None:
        self.cache: Dict[str, Any] = {}  # Simple file content cache
        self.cache_ttl: float = 300.0  # Cache TTL in seconds (5 minutes)

    async def _is_cache_expired(self, file_path: str) -> bool:
        """Checks if the cache entry for the file is expired."""
        if file_path not in self.cache:
            return True

        try:
            # Get the last modified time of the file
            current_time = time.time()
            stat = await aiofiles.os.stat(file_path)
            last_modified_time = stat.st_mtime

            # Check if the file was modified beyond the TTL
            cache_entry_time = self.cache[file_path].get("timestamp")
            if not cache_entry_time or (
                current_time - cache_entry_time > self.cache_ttl
            ):
                return True

            # Also check if the file itself has been modified
            if last_modified_time > cache_entry_time:
                return True

        except FileNotFoundError:
            _logger.error(f"File not found: {file_path}. Assuming cache is expired.")
            return True
        except Exception as e:
            _logger.error(f"Error checking cache expiration for {file_path}: {e!r}")
            return True

        return False

    async def read(self, file_path: Union[str, Path]) -> Any:
        """Reads the content of a file using the appropriate handler."""
        file_path_str = str(file_path)
        if not await self._is_cache_expired(file_path_str):
            _logger.info(f"Reading from cache: {file_path_str}")
            return self.cache[file_path_str]

        try:
            file_extension = Path(file_path_str).suffix[1:].lower()
            handler = get_handler(file_extension)
            content = await handler.read(file_path_str)
            self.cache[file_path_str] = content
            return content
        except FileNotFoundError as e:
            raise FileReadError(message="File not found", path=file_path_str) from e
        except Exception as e:
            raise FileReadError(message="Error reading file", path=file_path_str) from e

    async def write(self, file_path: Union[str, Path], content: Any) -> None:
        """Writes the content to a file using the appropriate handler."""
        file_path_str = str(file_path)
        try:
            file_extension = Path(file_path_str).suffix[1:].lower()
            handler = get_handler(file_extension)
            await handler.write(file_path_str, content)
            self.cache.pop(file_path_str, None)  # Invalidate cache on write
        except Exception as e:
            raise FileWriteError(
                message=f"Error writing to file: {e}", path=file_path_str
            ) from e

    async def read_lines(
        self, file_path: Union[str, Path], ignore_comments: bool = True
    ) -> List[str]:
        """Reads a file and returns a list of lines, optionally ignoring comments."""
        file_path_str = str(file_path)
        try:
            async with aiofiles.open(file_path_str, encoding="utf-8") as f:
                lines = await f.readlines()
                if ignore_comments:
                    lines = [
                        line.split("#")[0].strip()
                        for line in lines
                        if not line.strip().startswith("#")
                    ]
                return [line.strip() for line in lines if line.strip()]
        except FileNotFoundError as e:
            raise FileReadError(message="File not found", path=file_path_str) from e
        except Exception as e:
            raise FileReadError(message="Error reading file", path=file_path_str) from e

    async def batch_read(self, file_paths: List[Union[str, Path]]) -> Dict[str, Any]:
        """Reads multiple files and returns a dictionary of file paths and content."""
        results: Dict[str, Any] = {}
        for file_path in file_paths:
            try:
                results[str(file_path)] = await self.read(file_path)
            except FileReadError as e:
                print(f"Skipping file: {e}")
        return results

    async def find_files(
        self,
        directory: Union[str, Path],
        pattern: str,
        recursive: bool = True,
        ignore_list: Optional[List[str]] = None,
    ) -> List[Path]:
        """
        Finds files in a directory matching a pattern.
        """
        directory_path = Path(directory)
        if not directory_path.is_dir():
            raise ValueError(f"Invalid directory: {directory}")

        if ignore_list is None:
            ignore_list = []

        # Convert ignore list to a set of absolute paths for faster lookup
        ignore_paths = {directory_path / ignore for ignore in ignore_list}

        found_files: List[Path] = []
        if recursive:
            for path in directory_path.rglob("*"):
                if (
                    path.is_file()
                    and re.match(pattern, path.name)
                    and path.parent not in ignore_paths
                ):
                    found_files.append(path)
        else:
            for path in directory_path.glob("*"):
                if (
                    path.is_file()
                    and re.match(pattern, path.name)
                    and path not in ignore_paths
                ):
                    found_files.append(path)

        return found_files

    async def create_directories(self, file_path: Union[str, Path]) -> None:
        """Creates directories for a given file path if they don't exist."""
        path = Path(file_path)
        parent_dir = path.parent
        if not await aiofiles.os.path.exists(parent_dir):
            await aiofiles.os.makedirs(parent_dir, exist_ok=True)

    async def exists(self, file_path: Union[str, Path]) -> bool:
        """Checks if a file or directory exists."""
        return await aiofiles.os.path.exists(file_path)

    async def delete(self, file_path: Union[str, Path]) -> None:
        """Deletes a file or directory."""
        path = Path(file_path)
        if await aiofiles.os.path.isfile(path):
            await aiofiles.os.remove(path)
        elif await aiofiles.os.path.isdir(path):
            import shutil

            shutil.rmtree(path)  # Use with caution!
        else:
            raise FileNotFoundError(f"No such file or directory: {file_path}")
