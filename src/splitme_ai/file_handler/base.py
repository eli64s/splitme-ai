from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Union


class AbstractFileHandler(ABC):
    """
    Abstract base class for file handlers.

    Subclasses should implement the read() and write() methods for specific file types.
    """

    @abstractmethod
    async def read(self, file_path: Union[str, Path]) -> Any:
        """
        Reads the content of a file.

        Parameters
        ----------
        file_path : str or Path
            The path to the file.

        Returns
        -------
        Any
            The content of the file, parsed according to the file type.
        """
        ...

    @abstractmethod
    async def write(self, file_path: Union[str, Path], content: Any) -> None:
        """
        Writes the content to a file.

        Parameters
        ----------
        file_path : str or Path
            The path to the file.
        content : Any
            The content to write.
        """
        ...
