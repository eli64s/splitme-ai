"""MkDocs configuration generator with enhanced validation."""

from pathlib import Path
from typing import Dict, Optional, Union

from splitme_ai.generators.mkdocs.models import (
    MkDocsConfig,
    ThemeConfig,
    ThemePalette,
    ThemeType,
)
from splitme_ai.logger import Logger

_logger = Logger(__name__)


def create_mkdocs_config(
    docs_dir: Union[str, Path],
    site_name: str,
    enable_material: bool = True,
    theme_palette: Optional[Dict[str, str]] = None,
) -> MkDocsConfig:
    """Create a new MkDocs configuration instance."""
    theme_config = ThemeConfig(
        name=ThemeType.MATERIAL if enable_material else ThemeType.MKDOCS,
        palette=ThemePalette(**(theme_palette or {})),
    )
    _logger.debug(f"Creating MkDocs configuration with theme: {theme_config}")
    return MkDocsConfig(
        site_name=site_name, docs_dir=Path(docs_dir), theme=theme_config
    )
