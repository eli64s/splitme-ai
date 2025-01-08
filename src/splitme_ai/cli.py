"""Command-line interface implementation using Pydantic settings management."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    pass

from pydantic import AliasChoices, BaseModel, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from splitme_ai.file_manager import FileHandler
from splitme_ai.logger import Logger
from splitme_ai.settings import SplitmeSettings

_logger = Logger(__name__)
_file_handler = FileHandler()


class ConfigCommand(BaseModel):
    """
    CLI command for managing configurations via YAML files.
    """

    file: Path = Field(
        default=Path(".splitme.yaml"),
        description="Path to config file",
        validate_default=True,
    )
    generate: bool = Field(
        default=False, description="Generate default configuration file"
    )
    show: bool = Field(default=False, description="Show current configuration settings")

    model_config = SettingsConfigDict(validate_default=True, extra="forbid")

    @field_validator("file")
    def validate_file(cls, v: Union[str, Path]) -> Path:
        """Convert string to Path if necessary."""
        if isinstance(v, str):
            return Path(v)
        return v

    def _prepare_settings_for_yaml(
        self, settings_dict: SplitmeSettings
    ) -> Dict[str, Any]:
        """Convert settings to YAML-serializable format."""
        serializable_dict: Dict[str, Any] = {}
        for key, value in settings_dict.model_dump().items():
            if isinstance(value, Path):
                serializable_dict[key] = str(value)
            elif isinstance(value, list | set) and any(
                isinstance(x, Path) for x in value
            ):
                serializable_dict[key] = [
                    str(x) if isinstance(x, Path) else x for x in value
                ]
            else:
                serializable_dict[key] = value
        return serializable_dict

    async def cli_cmd(self) -> None:
        """Execute the config command."""
        if self.show:
            settings = SplitmeSettings()
            _logger.info("Current splitme-ai configuration:")
            for field, value in settings.model_dump().items():
                _logger.info(f"Field: {field}, Value: {value}")

        if self.generate:
            settings = SplitmeSettings()
            if self.file.exists():
                _logger.warning(
                    f"Configuration file {self.file} already exists. Exiting."
                )
            else:
                self.file.parent.mkdir(parents=True, exist_ok=True)
                yaml_content = self._prepare_settings_for_yaml(settings_dict=settings)
                await _file_handler.write(file_path=self.file, content=yaml_content)
                content = await _file_handler.read(self.file)
                _logger.info(
                    f"Generated configuration file {self.file} with content: {content[:50]}"
                )


class SplitCommand(BaseModel):
    """
    CLI command for splitting markdown files.
    """

    input_file: Path = Field(
        ...,
        description="Input markdown file to split",
        validation_alias=AliasChoices("i", "input"),
    )
    settings: SplitmeSettings = Field(
        default_factory=lambda: SplitmeSettings(),
        description="Configuration settings for text splitting.",
    )

    async def cli_cmd(self) -> None:
        """Execute the split command."""
        from splitme_ai.core import MarkdownSplitter

        splitter = MarkdownSplitter(self.settings)

        # content = self.input_file.read_text(encoding="utf-8")
        content = await _file_handler.read(self.input_file)
        _logger.info(f"Reading {self.input_file} content: {content[:200]}")

        sections = await splitter.process_file(content)
        _logger.info(f"Split {self.input_file} into {len(sections)} sections.")

        for section in sections:
            _logger.info(f"Created file {section.filename} from {section.title}")


class SplitmeApp(BaseSettings):
    """
    Main application CLI interface.
    """

    config: Optional[ConfigCommand] = Field(
        default=None, description="Manage configuration"
    )
    split: Optional[SplitCommand] = Field(
        default=None, description="Split markdown files"
    )
    version: bool = Field(default=False, description="Package version")

    model_config = SettingsConfigDict(
        case_sensitive=True,
        cli_enforce_required=True,
        cli_kebab_case=True,
        cli_implicit_flags=True,
        cli_parse_args=True,
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="SPLITME_",
        protected_namespaces=(),
        validate_default=True,
    )

    async def cli_cmd(self) -> None:
        """Execute the appropriate command."""
        if self.version:
            pypi_version = SplitmeSettings().version
            _logger.info(f"splitme-ai {pypi_version}")
        elif self.split:
            await self.split.cli_cmd()
        elif self.config:
            await self.config.cli_cmd()
