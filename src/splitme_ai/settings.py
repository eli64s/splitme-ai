from enum import StrEnum, auto
from pathlib import Path
from typing import Annotated, Optional, Set, Tuple, Type

from pydantic import AliasChoices, BaseModel, Field, field_validator, model_validator
from pydantic_settings import (
    BaseSettings,
    CliImplicitFlag,
    PydanticBaseSettingsSource,
    PyprojectTomlConfigSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)

from splitme_ai.generators.mkdocs.config import create_mkdocs_config
from splitme_ai.generators.mkdocs.models import ThemePalette, ThemeType
from splitme_ai.logger import Logger

_logger = Logger(__name__)


class HeadingLevel(StrEnum):
    """Enumeration for markdown heading levels."""

    H1 = auto()
    H2 = auto()
    H3 = auto()
    H4 = auto()
    H5 = auto()
    H6 = auto()


class OutputFormat(StrEnum):
    """Supported output formats."""

    MARKDOWN = auto()
    HTML = auto()
    PDF = auto()
    DOCX = auto()


class ContentAnalytics(BaseModel):
    """Configuration for content analysis features."""

    analytics_model: Optional[str] = Field(default=None)
    enable_keyword_extraction: bool = Field(default=False)
    enable_readability_scores: bool = Field(default=False)
    enable_summary_generation: bool = Field(default=False)
    enable_question_generation: bool = Field(default=False)


class MkDocsSettings(BaseModel):
    """MkDocs-specific configuration settings."""

    enable: CliImplicitFlag[bool] = Field(
        default=False,
        description="Generate MkDocs configuration",
    )
    theme: ThemeType = Field(
        default=ThemeType.MATERIAL,
        description="MkDocs theme to use",
    )
    palette: Optional[ThemePalette] = Field(
        default_factory=ThemePalette,
        description="Theme color palette configuration",
    )
    site_name: Optional[str] = Field(
        default=None,
        description="Custom site name (defaults to directory name)",
    )


class SplitOptions(BaseModel):
    """Advanced splitting configuration."""

    combine_short_sections: bool = Field(
        default=False, description="Combine sections shorter than min_content_length"
    )
    min_content_length: Optional[int] = Field(
        default=None, description="Minimum content length for a section", ge=0
    )
    preserve_images: bool = Field(
        default=True, description="Preserve and adjust image paths"
    )
    preserve_links: bool = Field(
        default=True, description="Preserve and adjust internal document links"
    )


class SplitmeSettings(BaseSettings):
    """
    Configuration settings for splitme-ai, including version from pyproject.toml.
    """

    content_analytics: ContentAnalytics = Field(
        default_factory=ContentAnalytics,
        description="Content analysis configuration",
    )
    split_options: SplitOptions = Field(
        default_factory=SplitOptions,
        description="Advanced splitting options",
    )
    heading_level: Annotated[
        HeadingLevel,
        Field(
            default=HeadingLevel.H2,
            description="Heading level to split on (1-6)",
            validation_alias=AliasChoices("hl", "heading_level"),
        ),
    ]
    output_dir: Annotated[
        Path,
        Field(
            default=Path(".splitme-ai/test-docs"),
            description="Output directory for split files",
            validation_alias=AliasChoices("o", "output"),
        ),
    ]
    output_format: Annotated[
        OutputFormat,
        Field(
            default=OutputFormat.MARKDOWN,
            description="Output file format",
            validation_alias=AliasChoices("f", "format"),
        ),
    ]
    case_sensitive: bool = Field(
        default=False, description="Use case-sensitive heading matching"
    )
    exclude_patterns: Set[str] = Field(
        default_factory=set,
        description="Patterns to exclude from splitting",
    )
    preserve_context: bool = Field(
        default=True, description="Preserve parent heading context in split files"
    )
    template_dir: Optional[Path] = Field(
        default=None,
        description="Custom template directory for output formats",
    )
    version: str | None = Field(
        default=None,
        description="Version of the splitme-ai application",
    )
    mkdocs: MkDocsSettings = Field(
        default_factory=MkDocsSettings,
        description="MkDocs configuration settings",
        validation_alias=AliasChoices("mk", "mkdocs"),
    )

    model_config = SettingsConfigDict(
        # env_file=".env",
        # env_file_encoding="utf-8",
        # env_nested_delimiter="__",
        # env_prefix="SPLITME_",
        case_sensitive=False,
        cli_implicit_flags=True,
        extra="ignore",
        pyproject_toml_table_header=("project",),
        yaml_file=[
            ".splitme.yaml",
            ".splitme.yml",
        ],
        populate_by_name=True,
        validate_default=True,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        """Customize settings sources - prioritize pyproject.toml."""
        yaml_source = YamlConfigSettingsSource(settings_cls)
        pyproject_source = PyprojectTomlConfigSettingsSource(settings_cls)
        return (
            pyproject_source,
            yaml_source,
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )

    @field_validator("output_dir")
    def validate_output_dir(cls, v: Path) -> Path:
        """Ensure output directory exists."""
        v.mkdir(parents=True, exist_ok=True)
        return v

    @model_validator(mode="after")
    def validate_analytics_config(self) -> "SplitmeSettings":
        """Validate analytics configuration."""
        if (
            any([
                self.content_analytics.enable_readability_scores,
                self.content_analytics.enable_keyword_extraction,
                self.content_analytics.enable_summary_generation,
            ])
            and not self.content_analytics.analytics_model
        ):
            raise ValueError(
                "Analytics model must be defined to enable content analysis features."
            )
        return self

    def process_mkdocs(self) -> None:
        """Generate MkDocs configuration file with enhanced settings."""
        if not self.mkdocs.enable:
            return

        config = create_mkdocs_config(
            docs_dir=self.output_dir,
            site_name=self.mkdocs.site_name
            or f"{self.output_dir.name.capitalize()} Documentation Site",
            enable_material=self.mkdocs.theme == ThemeType.MATERIAL,
            theme_palette=self.mkdocs.palette.model_dump()
            if self.mkdocs.palette
            else None,
        )

        _logger.info(f"Generating MkDocs configuration file at: {self.output_dir}")

        config.generate_config()
