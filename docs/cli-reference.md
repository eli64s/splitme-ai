---
title: CLI Reference
---

This page provides a comprehensive overview of the `splitme-ai` Command-Line Interface (CLI) and its available options.

```console
usage: splitme-ai [-h] [--config {JSON,null}]
                  [--config.generate | --no-config.generate]
                  [--config.show | --no-config.show] [--split {JSON,null}]
                  [--split.i Path] [--split.settings JSON]
                  [--split.settings.case-sensitive | --no-split.settings.case-sensitive]
                  [--split.settings.exclude-patterns Set[str]]
                  [--split.settings.mk | --no-split.settings.mk | --split.settings.mkdocs | --no-split.settings.mkdocs]
                  [--split.settings.hl str] [--split.settings.o Path]
                  [--split.settings.preserve-context | --no-split.settings.preserve-context]
                  [--version | --no-version]

Main application CLI interface.

options:
  -h, --help            show this help message and exit
  --version, --no-version
                        Package version (default: False)

config options:
  default: null (undefined)
  Manage configuration

  --config {JSON,null}  set config from JSON string
  --config.generate, --no-config.generate
                        Generate default configuration file. (default: False)
  --config.show, --no-config.show
                        Show current configuration settings. (default: False)

split options:
  default: null (undefined)
  Split markdown files

  --split {JSON,null}   set split from JSON string
  --split.i Path, --split.input Path
                        Input markdown file to split (ifdef: required)

split.settings options:
  default: null (undefined)
  Configuration settings for text splitting.

  --split.settings JSON
                        set split.settings from JSON string
  --split.settings.case-sensitive, --no-split.settings.case-sensitive
                        Use case-sensitive heading matching (default: False)
  --split.settings.exclude-patterns Set[str]
                        Patterns to exclude from splitting (default factory:
                        set)
  --split.settings.mk, --no-split.settings.mk, --split.settings.mkdocs, --no-split.settings.mkdocs
                        Generate MkDocs configuration (default: False)
  --split.settings.hl str, --split.settings.heading-level str
                        Heading level to split on (e.g., '#', '##', '###')
                        (default: ##)
  --split.settings.o Path, --split.settings.output Path
                        Output directory for split files (default: .splitme-
                        ai/output)
  --split.settings.preserve-context, --no-split.settings.preserve-context
                        Preserve parent heading context in split files
                        (default: True)
```

---
