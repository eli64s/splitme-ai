from typing import Dict, Type, Union

from splitme_ai.file_handler.base import AbstractFileHandler
from splitme_ai.file_handler.json_handler import JSONFileHandler
from splitme_ai.file_handler.text_handler import TextFileHandler
from splitme_ai.file_handler.toml_handler import TOMLFileHandler
from splitme_ai.file_handler.yaml_handler import YAMLFileHandler

_handler_registry: Dict[str, Type[AbstractFileHandler]] = {}


def register_handler(
    file_extensions: Union[str, list[str]], handler_class: Type[AbstractFileHandler]
):
    """Registers a handler class for given file extensions."""
    if isinstance(file_extensions, str):
        file_extensions = [file_extensions]
    for ext in file_extensions:
        _handler_registry[ext] = handler_class


def get_handler(file_extension: str) -> AbstractFileHandler:
    """Gets an instance of the handler for the given file extension."""
    handler_class = _handler_registry.get(file_extension)
    if not handler_class:
        raise ValueError(f"No handler found for file extension: {file_extension}")
    return handler_class()


# TODO: Add more file types as needed (e.g., CSV, TSV, XML, PDF, DOCX)
register_handler("json", JSONFileHandler)
register_handler("toml", TOMLFileHandler)
register_handler(["yaml", "yml"], YAMLFileHandler)
register_handler(["txt", "md", "html"], TextFileHandler)
