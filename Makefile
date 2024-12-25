SHELL := /bin/bash

# Project
PY_VERSION := 3.11
TARGET := src tests
TOML_FILE := pyproject.toml

# Tools
UV := uv
UVX := uvx --isolated
UV_PIP := $(UV) pip
UV_RUN := $(UV) run


# -- Clean Up ------------------------------------------------------------------

.PHONY: clean
clean: ## Clean build and virtual environment directories
	@echo -e "\n► Cleaning up project environment and directories..."
	-rm -rf dist/ .venv/ build/ *.egg-info/
	-find . -name "__pycache__" -type d -exec rm -rf {} +
	-find . -name "*.pyc" -type f -exec rm -f {} +


# -- Dependencies ------------------------------------------------------------

.PHONY: build-hatch
build-hatch: ## Build the distribution package using hatch
	hatch build
	pip show splitme-ai

.PHONY: build
build: ## Build the distribution package using uv
	uv build
	$(UV_PIP) install dist/splitme_ai-0.1.0-py3-none-any.whl

.PHONY: install
install: ## Install all project dependencies
	$(UV_PIP) install -r pyproject.toml --all-extras

.PHONY: install-editable
install-editable:: ## Install all project dependencies in editable mode
	$(UV_PIP) install -e ".[dev,docs,lint,test]"

.PHONY: lock
lock: ## Lock dependencies declared in pyproject.toml
	$(UV_PIP) compile pyproject.toml --all-extras

.PHONY: requirements
requirements: ## Generate requirements files from pyproject.toml
	$(UV_PIP) compile pyproject.toml -o requirements.txtiu
	$(UV_PIP) compile pyproject.toml --all-extras -o requirements-dev.txt

.PHONY: sync
sync: ## Sync environment with pyproject.toml
	uv sync --all-groups --dev

.PHONY: venv
venv: ## Create a virtual environment
	uv venv --python $(PY_VERSION)


# -- Documentation --------------------------------------------------------------

.PHONY: docs
docs: ## Build documentation site using mkdocs
	# $(UV_RUN) mkdocs build 
	# $(UV_RUN) mkdocs serve
	uvx --with mkdocs-material mkdocs serve


# -- Linting ---------------------------------------------------------------

.PHONY: format-toml
format-toml: ## Format TOML files using pyproject-fmt
	$(UVX) pyproject-fmt $(TOML_FILE) --indent 4

.PHONY: format
format: ## Format Python files using Ruff
	@echo -e "\n► Running the Ruff formatter..."
	$(UVX) ruff format $(TARGET) --config .ruff.toml

.PHONY: lint
lint: ## Lint Python files using Ruff
	@echo -e "\n ►Running the Ruff linter..."
	$(UVX) ruff check $(TARGET) --fix --config .ruff.toml

.PHONY: format-lint
format-lint: format lint ## Format and lint Python files


# -- Utilities ------------------------------------------------------------------

.PHONY: help
help: ## Display this help
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@awk 'BEGIN {FS = ":.*?## "; printf "\033[1m%-20s %-50s\033[0m\n", "Target", "Description"; \
	              printf "%-20s %-50s\n", "------", "-----------";} \
	      /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %-50s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""