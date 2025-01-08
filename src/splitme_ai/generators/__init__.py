"""Package initialization for generators module."""

from splitme_ai.generators.mkdocs.config import create_mkdocs_config
from splitme_ai.generators.mkdocs.models import MkDocsConfig

__all__ = ["MkDocsConfig", "create_mkdocs_config"]
