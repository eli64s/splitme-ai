from enum import StrEnum
from pathlib import Path
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field, model_validator


class ThemeType(StrEnum):
    """Supported MkDocs themes."""

    MATERIAL = "material"
    MKDOCS = "mkdocs"
    READTHEDOCS = "readthedocs"


class ThemePalette(BaseModel):
    """Material theme color palette configuration."""

    scheme: str = Field(default="default", description="Color scheme (default/slate)")
    primary: str = Field(default="indigo", description="Primary color")
    accent: str = Field(default="indigo", description="Accent color")

    @model_validator(mode="after")
    def validate_colors(self) -> "ThemePalette":
        """Validate color values against Material Design color palette."""
        valid_colors = {
            "red",
            "pink",
            "purple",
            "deep-purple",
            "indigo",
            "blue",
            "light-blue",
            "cyan",
            "teal",
            "green",
            "light-green",
            "lime",
            "yellow",
            "amber",
            "orange",
            "deep-orange",
            "brown",
            "grey",
            "blue-grey",
        }
        if self.primary not in valid_colors:
            raise ValueError(f"Invalid primary color. Must be one of: {valid_colors}")
        if self.accent not in valid_colors:
            raise ValueError(f"Invalid accent color. Must be one of: {valid_colors}")
        return self


class ThemeConfig(BaseModel):
    """MkDocs theme configuration."""

    name: ThemeType = Field(default=ThemeType.MATERIAL)
    palette: Optional[ThemePalette] = Field(default_factory=ThemePalette)
    features: List[str] = Field(
        default_factory=lambda: [
            "navigation.instant",
            "navigation.tracking",
            "navigation.tabs",
            "navigation.sections",
            "navigation.expand",
            "search.highlight",
        ]
    )

    @model_validator(mode="after")
    def validate_features(self) -> "ThemeConfig":
        """Validate theme features based on selected theme."""
        valid_material_features = {
            "navigation.instant",
            "navigation.tracking",
            "navigation.tabs",
            "navigation.sections",
            "navigation.expand",
            "search.highlight",
            "navigation.top",
            "search.suggest",
            "search.share",
        }

        if self.name == ThemeType.MATERIAL:
            invalid_features = set(self.features) - valid_material_features
            if invalid_features:
                raise ValueError(
                    f"Invalid Material theme features: {invalid_features}. "
                    f"Valid features are: {valid_material_features}"
                )
        return self


class MkDocsConfig(BaseModel):
    """Enhanced MkDocs configuration with validation."""

    site_name: str = Field(..., min_length=1)
    docs_dir: Path = Field(default=Path(".splitme-ai/"))
    site_description: Optional[str] = None
    site_author: Optional[str] = None
    site_url: Optional[str] = None

    theme: ThemeConfig = Field(default_factory=ThemeConfig)

    markdown_extensions: List[str] = Field(
        default_factory=lambda: [
            "admonition",
            "pymdownx.details",
            "pymdownx.superfences",
            "pymdownx.highlight",
            "pymdownx.inlinehilite",
            "pymdownx.snippets",
            "tables",
            "footnotes",
        ]
    )

    extra_css: List[Path] = Field(default_factory=list)
    extra_javascript: List[Path] = Field(default_factory=list)

    nav: List[Dict[str, str]] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_paths(self) -> "MkDocsConfig":
        """Validate that all paths exist."""
        if not self.docs_dir.exists():
            self.docs_dir.mkdir(parents=True, exist_ok=True)

        for css_file in self.extra_css:
            if not css_file.exists():
                raise ValueError(f"CSS file not found: {css_file}")

        for js_file in self.extra_javascript:
            if not js_file.exists():
                raise ValueError(f"JavaScript file not found: {js_file}")

        return self

    def generate_config(self, output_file: Optional[Union[str, Path]] = None) -> None:
        """Generate MkDocs configuration file with enhanced error handling."""
        import yaml

        if not output_file:
            output_file = self.docs_dir / "mkdocs.yml"

        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Convert model to dictionary, handling Path objects
        config_dict = self.model_dump()
        config_dict["docs_dir"] = str(config_dict["docs_dir"])
        if config_dict["extra_css"]:
            config_dict["extra_css"] = [str(p) for p in config_dict["extra_css"]]
        if config_dict["extra_javascript"]:
            config_dict["extra_javascript"] = [
                str(p) for p in config_dict["extra_javascript"]
            ]

        # Write configuration
        with output_path.open("w", encoding="utf-8") as f:
            yaml.dump(
                config_dict,
                f,
                default_flow_style=False,
                sort_keys=False,
                allow_unicode=True,
                indent=2,
            )
