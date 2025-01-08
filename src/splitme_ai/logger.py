"""Custom logger implementation with color and emoji support."""

import logging
import sys
from typing import Any, ClassVar, Dict

LOG_LEVEL_EMOJIS = {
    "DEBUG": "⚙︎",
    "INFO": "►",
    "WARNING": "⚠️",
    "ERROR": "ⓧ",
    "CRITICAL": "‼",
}

LOG_LEVEL_COLORS = {
    "DEBUG": "\033[34m",
    "INFO": "\033[35m",
    "WARNING": "\033[33m",
    "ERROR": "\033[31m",
    "CRITICAL": "\033[31m\033[1m",
}

RESET_COLOR = "\033[0m"


class CustomFormatter(logging.Formatter):
    """
    Custom logging formatter with color and emoji support.
    """

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record."""
        record.emoji = LOG_LEVEL_EMOJIS.get(record.levelname, "")
        record.color = LOG_LEVEL_COLORS.get(record.levelname, "")
        super().format(record)
        return f"{record.color}{record.emoji} {record.levelname} | {record.asctime} | {record.name} | {RESET_COLOR}{record.message}"


class Logger:
    """
    Custom logger class for the splitme-ai package.
    """

    _instances: ClassVar[Dict[str, "Logger"]] = {}
    _configured_loggers: ClassVar[set[str]] = set()

    def __new__(cls, name: str, level: int = logging.DEBUG) -> "Logger":
        """Creates a new logger instance."""
        if name not in cls._instances:
            instance = super().__new__(cls)
            instance._name = name
            instance._level = level
            instance._logger = logging.getLogger(name)
            if name not in cls._configured_loggers:
                instance._configure_logger()
                cls._configured_loggers.add(name)
            cls._instances[name] = instance
        return cls._instances[name]

    def __init__(self, name: str, level: int = logging.DEBUG) -> None:
        """Initialize is called after __new__, but we handle everything in __new__."""
        pass

    def _configure_logger(self) -> None:
        """Configures the logger."""
        formatter = CustomFormatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(self._level)
        # Prevent propagation to prevent duplicate logs
        self._logger.propagate = False

    def info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Logs an info message."""
        self._logger.info(msg, *args, **kwargs)

    def debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Logs a debug message."""
        self._logger.debug(msg, *args, **kwargs)

    def warning(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Logs a warning message."""
        self._logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Logs an error message."""
        self._logger.error(msg, *args, **kwargs)

    def critical(self, msg: str, *args: Any, **kwargs: Any) -> None:
        """Logs a critical message."""
        self._logger.critical(msg, *args, **kwargs)

    def log(self, level: int, msg: str, *args: Any, **kwargs: Any) -> None:
        """Logs a message at the specified level."""
        self._logger.log(level, msg, *args, **kwargs)
