<div id="top">

<p align="center">
  <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/svg/readme-ai-gradient.svg" alt="readme-ai" width="85%">
</p>

<p align="center">
  <em>Designed for simplicity, customization, and developer productivity.</em>
</p>

<p align="center">
  <a href="https://github.com/eli64s/readme-ai/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/eli64s/readme-ai/release-pipeline.yml?logo=githubactions&label=CI&logoColor=white&color=4169E1" alt="Github Actions">
  </a>
  <a href="https://app.codecov.io/gh/eli64s/readme-ai">
    <img src="https://img.shields.io/codecov/c/github/eli64s/readme-ai?logo=codecov&logoColor=white&label=Coverage&color=5D4ED3" alt="Test Coverage">
  </a>
  <a href="https://pypi.python.org/pypi/readmeai/">
    <img src="https://img.shields.io/pypi/v/readmeai?logo=Python&logoColor=white&label=PyPI&color=7934C5" alt="PyPI Version">
  </a>
  <a href="https://www.pepy.tech/projects/readmeai">
    <img src="https://img.shields.io/pepy/dt/readmeai?logo=PyPI&logoColor=white&label=Downloads&color=9400D3" alt="Total Downloads">
  </a>
  <a href="https://opensource.org/license/mit/">
    <img src="https://img.shields.io/github/license/eli64s/readme-ai?logo=opensourceinitiative&logoColor=white&label=License&color=8A2BE2" alt="MIT License">
  </a>
</p>

</div>

<img src="readmeai/data/svg/gradient_line_4169E1_8A2BE2.svg" alt="line break" width="100%" height="4px">

## Quick Links

- [Intro](#introduction)
- [Demo](#demo)
- [Features](#features)
- [Quickstart](#getting-started)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributing](#contributing)

> [!IMPORTANT]
> Visit the [Official Documentation][docs] for detailed guides and tutorials.

<img src="readmeai/data/svg/gradient_line_4169E1_8A2BE2.svg" alt="line break" width="100%" height="3px">

## Introduction

ReadmeAI is a developer tool that automatically generates README files using a robust repository processing engine and advanced language models. Simply provide a URL or path to your codebase, and a well-structured and detailed README will be generated.

**Why Use ReadmeAI?**

This project aims to streamline the process of creating and maintaining documentation across all technical disciplines and experience levels. The core principles include:

- **🔵 Automate:** Generate detailed and structured README files with a single command.
- **⚫️ Customize:** Select from a variety of templates, styles, badges, and much more.
- **🟣 Flexible:** Switch between `OpenAI`, `Ollama`, `Anthropic`, and `Gemini` anytime.
- **🟠 Language Agnostic:** Compatible with a wide range of languages and frameworks.
- **🟡 Best Practices:** Ensure clean and consistent documentation across all projects.
- **✨ Offline Mode:** Create README files offline, without using a LLM API service.

## Demo

**Run from your terminal:**

[readmeai-cli-demo][cli-demo]

<!--
**Run from your browser:**

[readmeai-streamlit-demo][streamlit-demo]
-->

<img src="readmeai/data/svg/gradient_line_4169E1_8A2BE2.svg" alt="line break" width="100%" height="3px">

## Features

Let's begin by exploring various customization options and styles supported by ReadmeAI:

<div align="left">
  <!-- HEADER STYLES & THEMES -->
  <h6>Header Styles & Themes</h6>
  <table>
    <tr>
      <td align="left">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/custom-dragon.png"
             alt="custom-dragon-project-logo"
             width="800"
             style="border: 1px solid #E7E9EB; border-radius: 5px; padding: 5px;">
        <p align="left"><b>CLI Command:</b></p>
        <pre align="left"><code>$ readme --repository https://github.com/eli64s/readme-ai-streamlit \
        &emsp13;--logo custom \
        &emsp13;--badge-color FF4B4B \
        &emsp13;--badge-style flat-square \
        &emsp13;--header-style classic
        </code></pre>
      </td>
    </tr>
    <tr>
      <td align="left">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/examples/toc/roman-numeral.png"
             alt="docker-go-readme-example"
             width="800"
             style="border: 1px solid #E7E9EB; border-radius: 5px; padding: 5px;">
        <p align="left"><b>CLI Command:</b></p>
        <pre align="left"><code>$ readme --repository https://github.com/olliefr/docker-gs-ping \
        &emsp13;--badge-color 00ADD8 \
        &emsp13;--badge-style for-the-badge \
        &emsp13;--header-style modern \
        &emsp13;--navigation-style roman
        </code></pre>
      </td>
    </tr>
  </table>

  <!-- ARTISTIC STYLES -->
  <h3>Banner Styles</h3>
  <table>
    <tr>
      <td align="left">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/ascii-art.png"
          alt="ascii-readme-header-style"
          width="800"
          style="border: 1px solid #E7E9EB; border-radius: 5px; padding: 5px;">
        <p align="left"><b>CLI Command:</b></p>
        <pre align="left"><code>$ readme --repository https://github.com/eli64s/readme-ai \
        &emsp13;--header-style ascii</code></pre>
      </td>
    </tr>
    <tr>
      <td align="left">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/svg-banner.png"
          alt="svg-banner"
          width="800"
          style="border: 1px solid #E7E9EB; border-radius: 5px; padding: 5px;">
        <p align="left"><b>CLI Command:</b></p>
        <pre align="left"><code>$ readme --repository https://github.com/eli64s/readme-ai-streamlit \
        &emsp13;--badge-style for-the-badge \
        &emsp13;--header-style svg</code></pre>
      </td>
    </tr>
  </table>

  <!-- LOGO VARIATIONS -->
  <h3>And More!</h3>
  <table>
    <tr>
      <td align="left" style="padding: 20px;">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/refs/heads/main/docs/docs/assets/img/headers/cloud.png"
            alt="cloud-logo"
            width="800"
            style="border: 1px solid #E7E9EB; border-radius: 5px; padding: 5px; margin-bottom: 15px;">
        <p align="left" style="margin: 10px 0;"><b>CLI Command:</b></p>
        <pre align="left"><code>$ readme --repository https://github.com/jwills/buenavista \
          &emsp13;--align left \
          &emsp13;--badge-style flat-square \
          &emsp13;--logo cloud</code></pre>
      </td>
    </tr>
  </table>

  <table>
    <tr>
      <td align="left" width="50%" style="padding: 20px;">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/custom-balloon.png"
            alt="balloon-logo"
            width="100%"
            style="border: 1px solid #E7E9EB; border-radius: 5px; padding: 5px; margin-bottom: 15px;">
        <p align="left" style="margin: 10px 0;"><b>CLI Command:</b></p>
        <pre align="left"><code>$ readme --repository https://github.com/eli64s/readme-ai-streamlit \
          &emsp13;--badge-style flat \
          &emsp13;--logo custom</code></pre>
        <pre align="left" style="margin-top: 10px;"><code>$ Provide an image file path or URL: \
          &emsp13;https://www.svgrepo.com/show/395851/balloon.svg</code></pre>
      </td>
      <td align="left" width="50%" style="padding: 20px;">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/skill-icons-light.png"
            alt="skill-icons"
            width="100%"
            style="border: 1px solid #E7E9EB; border-radius: 5px; padding: 5px; margin-bottom: 15px;">
        <p align="left" style="margin: 10px 0;"><b>CLI Command:</b></p>
        <pre align="left"><code>$ readme --repository https://github.com/FerrariDG/async-ml-inference \
          &emsp13;--badge-style skills-light \
          &emsp13;--logo grey</code></pre>
      </td>
    </tr>
  </table>

  <table>
    <tr>
      <td align="left" width="50%" style="padding: 20px;">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/headers/compact.png"
            alt="compact-header"
            width="100%"
            style="border: 1px solid #E7E9EB; border-radius: 5px; padding: 5px; margin-bottom: 15px;">
        <p align="left" style="margin: 10px 0;"><b>CLI Command:</b></p>
        <pre align="left"><code>$ readme --repository https://github.com/eli64s/readme-ai \
          &emsp13;--logo cloud \
          &emsp13;--header-style compact \
          &emsp13;--navigation-style fold</code></pre>
      </td>
      <td align="left" width="50%" style="padding: 20px;">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/refs/heads/main/docs/docs/assets/img/headers/modern-flat-square.png"
            alt="modern-style"
            width="100%"
            style="border: 1px solid #E7E9EB; border-radius: 5px; padding: 5px; margin-bottom: 15px;">
        <p align="left" style="margin: 10px 0;"><b>CLI Command:</b></p>
        <pre align="left"><code>$ readme --repository https://github.com/eli64s/readme-ai \
          &emsp13;-i custom \
          &emsp13;-bc BA0098 \
          &emsp13;-bs flat-square \
          &emsp13;-hs modern \
          &emsp13;-ns fold</code></pre>
      </td>
    </tr>
  </table>
</div>

> [!IMPORTANT]
> See the [Official Documentation][docs] for a complete list of customization options and examples.

Explore additional content sections supported by ReadmeAI:

<details closed>
  <summary><strong>🔹 Overview</strong></summary><br>
  <table>
    <tr>
      <td>
      <b>Overview</b><br>
        <p>◎ The <code>Overview</code> section provides a high-level summary of the project, including its use case, benefits, and differentiating features.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/llm-content/overview.png" alt="readme-overview-section" width="700">
      </td>
    </tr>
  </table>
</details>

<details closed>
  <summary><strong>🔸 Features</strong></summary><br>
  <table>
    <tr>
      <td><b>Features Table</b><br>
        <p>◎ Generated markdown table that highlights the key technical features and components of the codebase. This table is generated using a structured <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/prompts.toml">prompt template.</a>
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/llm-content/features-table.png" alt="readme-features-section" width="700">
      </td>
    </tr>
  </table>
</details>

<details closed>
  <summary><strong>🔶 Module Analysis</strong></summary><br>
  <table>
    <tr>
      <td><b>Directory Tree</b><br>
        <p>◎ The project's directory structure is generated using pure Python and embedded in the README. See <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/generators/tree.py">readmeai.generators.tree.</a> for more details.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/project-structure/tree.png" alt="directory-tree" width="700">
      </td>
    </tr>
    <tr>
      <td style="padding-top:20px;">
        <b>File Summaries</b><br>
        <p>◎ Summarizes key modules of the project, which are also used as context for downstream <a href="https://github.com/eli64s/readme-ai/blob/main/readmeai/config/settings/prompts.toml">prompts.</a>
        </p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/project-structure/file-summaries.png" alt="file-summaries" width="700">
    </tr>
  </table>
</details>

<details closed>
  <summary><strong>🔺 Quickstart Guides</strong></summary>
  <br>
  <table>
    <tr>
      <td><b>Getting Started</b><br>
        <p>◎ Prerequisites and system requirements are extracted from the codebase during preprocessing. The <a href="https://github.com/eli64s/readme-ai/tree/main/readmeai/parsers">parsers</a> handles the majority of this logic currently.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/getting-started/prerequisites-and-installation.png" alt="getting-started-section-prerequisites" width="700">
      </td>
    </tr>
    <tr>
      <td><b>Installation Guide</b><br>
        <p>◎ <code>Installation</code>, <code>Usage</code>, and <code>Testing</code> guides are generated based on the project's dependency files and codebase configuration.
        </p>
        <tr>
        <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/getting-started/usage-and-testing.png" alt="getting-started-section-usage-and-testing" width="700">
      </td>
    </tr>
  </table>
</details>

<details closed>
  <summary><strong>🔻 Contributing Guidelines</strong></summary>
  <br>
  <table>
    <tr>
      <td><b>Contributing Guide</b><br>
        <p>◎ Dropdown section that outlines general process for contributing to your project.</p>
        <p>◎ Provides links to your contributing guidelines, issues page, and more resources.</p>
        <p>◎ Graph of contributors is also included.</p>
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/contributing/contributing-guidelines.png" alt="contributing-guidelines-section" width="700">
      </td>
    </tr>
    <tr>
      <td><b>Additional Sections</b><br>
        <p>◎ <code>Roadmap</code>, <code>Contributing Guidelines</code>, <code>License</code>, and <code>acknowledgment</code> are included by default.
        </p>
      </td>
    </tr>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/eli64s/readme-ai/main/docs/docs/assets/img/contributing/footer.png" alt="footer-readme-section" width="700"></td>
    </tr>
  </table>
</details>

<img src="readmeai/data/svg/gradient_line_4169E1_8A2BE2.svg" alt="line break" width="100%" height="3px">

## Getting Started

### Prerequisites

ReadmeAI requires Python 3.9 or higher, plus one installation method of your choice:

| Requirement                          | Details                          |
|--------------------------------------|----------------------------------|
| • [Python][python-link] ≥3.9         | Core runtime                     |
| **Installation Method** (choose one) |                                  |
| • [pip][pip-link]                    | Default Python package manager   |
| • [pipx][pipx-link]                  | Isolated environment installer   |
| • [uv][uv-link]                      | High-performance package manager |
| • [docker][docker-link]              | Containerized environment        |

### Supported Repository Platforms

ReadmeAI needs access to your repository to generate a README file. Current supported platforms include:

| Platform                   | Details                   |
|----------------------------|---------------------------|
| [File System][file-system] | Local repository access   |
| [GitHub][github]           | Industry-standard hosting |
| [GitLab][gitlab]           | Full DevOps integration   |
| [Bitbucket][bitbucket]     | Atlassian ecosystem       |

### Supported LLM API Services

ReadmeAI is model agnostic, with support for the following LLM API services:

| Provider                     | Best For        | Details                  |
|------------------------------|-----------------|--------------------------|
| [OpenAI][openai]             | General use     | Industry-leading models  |
| [Anthropic][anthropic]       | Advanced tasks  | Claude language models   |
| [Google Gemini][gemini]      | Multimodal AI   | Latest Google technology |
| [Ollama][ollama]             | Open source     | No API key needed        |
| [Offline Mode][offline-mode] | Local operation | No internet required     |

---

### Installation

ReadmeAI is available on [PyPI][pypi-link] as readmeai and can be installed as follows:

<!-- #### Using `pip` [![pypi][pypi-shield]][pypi-link] -->

#### ![pip][python-svg]{ width="2%" }&emsp13;Pip

Install with pip (recommended for most users):

```sh
❯ pip install -U readmeai
```

<!-- #### Using `pipx` [![pipx][pipx-shield]][pipx-link] -->

#### ![pipx][pipx-svg]{ width="2%" }&emsp13;Pipx

With `pipx`, readmeai will be installed in an isolated environment:

```sh
❯ pipx install readmeai
```

#### ![uv][uv-svg]{ width="2%" }&emsp13;Uv

The fastest way to install readmeai is with [uv][uv-link]:

```sh
❯ uv tool install readmeai
```

<!-- #### Using `docker` [![docker][docker-shield]][docker-link] -->

#### ![docker][docker-svg]{ width="2%" }&emsp13;Docker

To run `readmeai` in a containerized environment, pull the latest image from [Docker Hub][dockerhub-link]:

```sh
❯ docker pull zeroxeli/readme-ai:latest
```

#### ![build-from-source][git-svg]{ width="2%" }&emsp13;From source

<details><summary><i>Click to build <code>readmeai</code> from source</i></summary>

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/eli64s/readme-ai
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd readme-ai
    ```

3. **Install dependencies:**

    ```sh
    ❯ pip install -r setup/requirements.txt
    ```

Alternatively, use the [setup script][setup-script] to install dependencies:

#### ![bash][bash-svg]{ width="2%" }&emsp13;Bash

1. **Run the setup script:**

    ```sh
    ❯ bash setup/setup.sh
    ```

Or, use `poetry` to build and install project dependencies:

#### ![poetry][poetry-svg]{ width="2%" }&emsp13;Poetry

1. **Install dependencies with poetry:**

    ```sh
    ❯ poetry install
    ```

</details>
<br>

### Additional Optional Dependencies

> [!IMPORTANT]
> To use the **Anthropic** and **Google Gemini** clients, extra dependencies are required. Install the package with the following extras:
>
> - **Anthropic:**
>   ```sh
>   ❯ pip install "readmeai[anthropic]"
>   ```
> - **Google Gemini:**
>   ```sh
>   ❯ pip install "readmeai[google-generativeai]"
>   ```
>
> - **Install Multiple Clients:**
>   ```sh
>   ❯ pip install "readmeai[anthropic,google-generativeai]"
>   ```

### Usage

#### Set your API key

When running `readmeai` with a third-party service, you must provide a valid API key. For example, the `OpenAI` client is set as follows:

```sh
❯ export OPENAI_API_KEY=<your_api_key>

# For Windows users:
❯ set OPENAI_API_KEY=<your_api_key>
```

<details closed><summary>Click to view environment variables for - <code>Ollama</code>, <code>Anthropic</code>, <code>Google Gemini</code></summary>
<br>
<details closed><summary>Ollama</summary>
<br>

Refer to the [Ollama documentation][ollama] for more information on setting up the Ollama server.

To start, follow these steps:

1. Pull your model of choice from the Ollama repository:

	```sh
	❯ ollama pull llama3.2:latest
	```

2. Start the Ollama server and set the `OLLAMA_HOST` environment variable:

	```sh
	❯ export OLLAMA_HOST=127.0.0.1 && ollama serve
	```

</details>
<details closed><summary>Anthropic</summary>

1. Export your Anthropic API key:

	```sh
	❯ export ANTHROPIC_API_KEY=<your_api_key>
	```

</details>
<details closed><summary>Google Gemini</summary>

1. Export your Google Gemini API key:

	```sh
	❯ export GOOGLE_API_KEY=<your_api_key
	```

</details>
</details>

#### Using the CLI

##### Running with a LLM API service

Below is the minimal command required to run `readmeai` using the `OpenAI` client:

```sh
❯ readmeai --api openai -o readmeai-openai.md -r https://github.com/eli64s/readme-ai
```

> [!IMPORTANT]
> The default model set is `gpt-3.5-turbo`, offering the best balance between cost and performance.When using any model from the `gpt-4` series and up, please monitor your costs and usage to avoid unexpected charges.

ReadmeAI can easily switch between API providers and models. We can run the same command as above with the `Anthropic` client:
```sh
❯ readmeai --api anthropic -m claude-3-5-sonnet-20240620 -o readmeai-anthropic.md -r https://github.com/eli64s/readme-ai
```

And finally, with the `Google Gemini` client:

```sh
❯ readmeai --api gemini -m gemini-1.5-flash -o readmeai-gemini.md -r https://github.com/eli64s/readme-ai
```

##### Running with local models

We can also run `readmeai` with free and open-source locally hosted models using the Ollama:

```sh
❯ readmeai --api ollama --model llama3.2 -r https://github.com/eli64s/readme-ai
```

##### Running on a local codebase

To generate a README file from a local codebase, simply provide the full path to the project:

```sh
❯ readmeai --repository /users/username/projects/myproject --api openai
```

Adding more customization options:

```sh
❯ readmeai --repository https://github.com/eli64s/readme-ai \
           --output readmeai.md \
           --api openai \
           --model gpt-4 \
           --badge-color A931EC \
           --badge-style flat-square \
           --header-style compact \
           --navigation-style fold \
           --temperature 0.9 \
           --tree-depth 2
           --logo LLM \
           --emojis solar
```

##### Running in offline mode

ReadmeAI supports `offline mode`, allowing you to generate README files without using a LLM API service.

```sh
❯ readmeai --api offline -o readmeai-offline.md -r https://github.com/eli64s/readme-ai
```

#### ![docker][docker-svg]{ width="2%" }&emsp13;Docker

Run the `readmeai` CLI in a Docker container:

```sh
❯ docker run -it --rm \
    -e OPENAI_API_KEY=$OPENAI_API_KEY \
    -v "$(pwd)":/app zeroxeli/readme-ai:latest \
    --repository https://github.com/eli64s/readme-ai \
    --api openai
```

#### ![streamlit][streamlit-svg]{ width="2%" }&emsp13;Streamlit

Try readme-ai directly in your browser on Streamlit Cloud, no installation required.

[<img align="center" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" width="20%">][streamlit]

See the [readme-ai-streamlit][readme-ai-streamlit] repository on GitHub for more details about the application.

> [!WARNING]
> The readme-ai Streamlit web app may not always be up-to-date with the latest features. Please use the command-line interface (CLI) for the most recent functionality.

#### ![build-from-source][git-svg]{ width="2%" }&emsp13;From source

<details><summary><i>Click to run <code>readmeai</code> from source</i></summary>

#### ![bash][bash-svg]{ width="2%" }&emsp13;Bash

If you installed the project from source with the bash script, run the following command:

1. Activate the virtual environment:

   ```sh
   ❯ conda activate readmeai
   ```

2. Run the CLI:

   ```sh
   ❯ python3 -m readmeai.cli.main -r https://github.com/eli64s/readme-ai
	```

#### ![poetry][poetry-svg]{ width="2%" }&emsp13;Poetry

1. Activate the virtual environment:

   ```sh
   ❯ poetry shell
   ```

2. Run the CLI:

   ```sh
   ❯ poetry run python3 -m readmeai.cli.main -r https://github.com/eli64s/readme-ai
   ```

</details>

<img src="readmeai/data/svg/gradient_line_4169E1_8A2BE2.svg" alt="line break" width="100%" height="3px">

### Testing

<!-- #### Using `pytest` [![pytest][pytest-shield]][pytest-link] -->

The [pytest][pytest-link] and [nox][nox-link] frameworks are used for development and testing.

Install the dependencies with uv:

```sh
❯ uv pip install -r pyproject.toml --all-extras
```

Run the unit test suite using Pytest:

```sh
❯ make test
```

Using nox, test the app against Python versions `3.9`, `3.10`, `3.11`, and `3.12`:

```sh
❯ make test-nox
```

> [!TIP]
> <sub>Nox is an automation tool for testing applications in multiple environments. This helps ensure your project is compatible with across Python versions and environments.</sub>

<img src="readmeai/data/svg/gradient_line_4169E1_8A2BE2.svg" alt="line break" width="100%" height="3px">

## Configuration

Customize your README generation with a variety of options and style settings supported such as:

| Option            | Description                                   | Default           |
|-------------------|-----------------------------------------------|-------------------|
| `--align`         | Text alignment in header                      | `center`          |
| `--api`           | LLM API service provider                      | `offline`         |
| `--badge-color`   | Badge color name or hex code                  | `0080ff`          |
| `--badge-style`   | Badge icon style type                         | `flat`            |
| `--header-style`  | Header template style                         | `classic`         |
| `--navigation-style` 	  | Table of contents style 				              | `bullet` 			    |
| `--emojis`        | Emoji theme packs prefixed to section titles  | `None`            |
| `--logo`         | Project logo image                             | `blue`            |
| `--logo-size`     | Logo image size                               | `30%`              |
| `--model`         | Specific LLM model to use                     | `gpt-3.5-turbo`   |
| `--output`        | Output filename                               | `readme-ai.md`    |
| `--repository`    | Repository URL or local directory path        | `None`            |
| `--temperature`   | Creativity level for content generation       | `0.1`             |
| `--tree-depth`    | Maximum depth of the directory tree structure | `2`               |

Run the following command to view all available options:

```sh
❯ readmeai --help
```

<sub>

Visit the [Official Documentation][docs] for a complete guide on configuring and customizing README files.
</sub>

<img src="readmeai/data/svg/gradient_line_4169E1_8A2BE2.svg" alt="line break" width="100%" height="3px">

## Examples

Explore a variety of README examples generated by `readmeai`:

| Tech | Output | Source | Description |
|------------|---------------|------------|-------------|
| Readme-ai | [readme-ai.md][default] | [readme-ai][readme-ai] | Readme-ai project |
| Apache Flink | [readme-pyflink.md][modern-header] | [pyflink-poc][pyflink] | Pyflink project |
| Streamlit | [readme-streamlit.md][svg-banner] | [readme-ai-streamlit][streamlit] | Streamlit web app |
| Vercel & NPM | [readme-vercel.md][dalle-logo] | [github-readme-quotes][vercel] | Vercel deployment |
| Go & Docker | [readme-docker-go.md][for-the-badge] | [docker-gs-ping][docker-golang] | Dockerized Go app |
| FastAPI & Redis | [readme-fastapi-redis.md][fastapi-redis] | [async-ml-inference][fastapi] | Async ML inference service |
| Java | [readme-java.md][compact-header] | [Minimal-Todo][java] | Minimalist todo Java app |
| PostgreSQL & DuckDB | [readme-postgres.md][classic-header] | [Buenavista][postgres] | Postgres proxy server |
| Kotlin | [readme-kotlin.md][readme-kotlin] | [android-client][kotlin] | Android client app |
| Offline Mode | [offline-mode.md][offline-mode] | [litellm][litellm] | LLM API service |

<sub>

Find additional README.md file examples in our [examples directory][examples-directory].

</sub>

<img src="readmeai/data/svg/gradient_line_4169E1_8A2BE2.svg" alt="line break" width="100%" height="3px">

## Roadmap

* [ ] Release `readmeai 1.0.0` with enhanced documentation management features.
* [ ] Develop `Vscode Extension` to generate README files directly in the editor.
* [ ] Develop `GitHub Actions` to automate documentation updates.
* [ ] Add `badge packs` to provide additional badge styles and options.
  + [ ] Code coverage, CI/CD status, project version, and more.

## Contributing

Contributions are welcome! Please read the [Contributing Guide][contributing] to get started.

- **💡 [Contributing Guide][contributing]**: Learn about our contribution process and coding standards.
- **🐛 [Report an Issue][github-issues]**: Found a bug? Let us know!
- **💬 [Start a Discussion][github-discussions]**: Have ideas or suggestions? We'd love to hear from you.

<br>

<p align="left">
  <a href="https://github.com{/eli64s/readme-ai/}graphs/contributors">
    <img src="https://contrib.rocks/image?repo=eli64s/readme-ai">
  </a>
</p>

## Acknowledgments

A big shoutout to the projects below for their awesome work and open-source contributions:

<div style="display: flex; align-items: left;">
  <a href="https://shields.io/">
    <img src="https://avatars.githubusercontent.com/u/6254238?s=200&v=4" alt="shields.io" style="width: 50px; margin-right: 10px;">
  </a>
  <a href="https://simpleicons.org/">
    <img src="https://avatars.githubusercontent.com/u/29872746?s=200&v=4" alt="simpleicons.org" style="width: 50px; margin-right: 10px;">
  </a>
  <a href="https://github.com/tandpfun/skill-icons">
    <img src="https://avatars.githubusercontent.com/u/28990589?v=4" alt="tandpfun/skill-icons" style="width: 50px; margin-right: 10px;">
  </a>
  <a href="https://github.com/astrit/css.gg">
    <img src="https://avatars.githubusercontent.com/u/2398447?v=4" alt="astrit/css.gg" style="width: 50px; margin-right: 10px;">
  </a>
  <a href="https://github.com/Ileriayo/markdown-badges">
    <img src="https://avatars.githubusercontent.com/u/31800695?v=4" alt="Ileriayo/markdown-badges" style="width: 50px; margin-right: 10px;">
  </a>
  <a href="https://github.com/Ileriayo/markdown-badges">
    <img src="https://avatars.githubusercontent.com/u/13166712?v=4" alt="Ileriayo/markdown-badges" style="width: 50px; margin-right: 10px;">
  </a>
</div>

<img src="readmeai/data/svg/gradient_line_4169E1_8A2BE2.svg" alt="line break" width="100%" height="3px">

## 🎗 License

Copyright © 2023 [readme-ai][readme-ai]. <br />
Released under the [MIT][license] license.

<div align="left">

[![][to-the-top]](#top)

</div>

<!-- REFERENCE LINKS -->

<!-- README-AI RESOURCES -->
[readme-ai]: https://github.com/eli64s/readme-ai
[readme-ai-streamlit]: https://github.com/eli64s/readme-ai-streamlit
[actions]: https://github.com/eli64s/readme-ai/actions
[codecov]: https://app.codecov.io/gh/eli64s/readme-ai
[docs]: https://eli64s.github.io/readme-ai
[github-discussions]: https://github.com/eli64s/readme-ai/discussions
[github-issues]: https://github.com/eli64s/readme-ai/issues
[github-pulls]: https://github.com/eli64s/readme-ai/pulls
[mit]: https://opensource.org/license/mit
[pepy]: https://www.pepy.tech/projects/readmeai
[contributing]: https://github.com/eli64s/readme-ai/blob/main/CONTRIBUTING.md
[license]: https://github.com/eli64s/readme-ai/blob/main/LICENSE
[to-the-top]: https://img.shields.io/badge/Return-5D4ED3?style=flat&logo=ReadMe&logoColor=white

<!-- README-AI DEMOS -->
[cli-demo]: https://github.com/user-attachments/assets/e1198922-5233-4a44-a5a8-15fa1cc4e2d7
[streamlit-demo]: https://github.com/user-attachments/assets/c3f60665-4768-4baa-8e31-6b6e8c4c9248

<!-- THIRD-PARTY RESOURCES -->
[docker-shield]: https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white
[docker-link]: https://hub.docker.com/r/zeroxeli/readme-ai
[python-link]: https://www.python.org/
[pip-link]: https://pip.pypa.io/en/stable/
[pypi-shield]: https://img.shields.io/badge/PyPI-3775A9.svg?style=flat&logo=PyPI&logoColor=white
[pypi-link]: https://pypi.org/project/readmeai/
[pipx-shield]: https://img.shields.io/badge/pipx-2CFFAA.svg?style=flat&logo=pipx&logoColor=black
[pipx-link]: https://pipx.pypa.io/stable/
[uv-link]: https://docs.astral.sh/uv/
[pytest-shield]: https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white
[pytest-link]: https://docs.pytest.org/en/7.1.x/contents.html
[nox-link]: https://nox.thea.codes/en/stable/
[streamlit-link]: https://readme-ai.streamlit.app/

<!-- BADGES & ICONS -->
[shieldsio]: https://shields.io/
[simple-icons]: https://simpleicons.org/
[skill-icons]: https://github.com/tandpfun/skill-icons
[github-profile-badges]: https://github.com/Aveek-Saha/GitHub-Profile-Badges
[markdown-badges]: https://github.com/Ileriayo/markdown-badges
[css-icons]: https://github.com/astrit/css.gg

[python-svg]: https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/python.svg
[pipx-svg]: https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/pipx.svg
[uv-svg]: https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/astral.svg
[docker-svg]: https://raw.githubusercontent.com/eli64s/readme-ai/3052baaca03db99d00808acfec43a44e81ecbf7f/docs/docs/assets/svg/docker.svg
[git-svg]: https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/git.svg
[bash-svg]: https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/gnubash.svg
[poetry-svg]: https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/poetry.svg
[streamlit-svg]: https://raw.githubusercontent.com/eli64s/readme-ai/5ba3f704de2795e32f9fdb67e350caca87975a66/docs/docs/assets/svg/streamlit.svg

<!-- GIT HOST PROVIDERS -->
[file-system]: https://en.wikipedia.org/wiki/File_system
[github]: https://github.com/
[gitlab]: https://gitlab.com/
[bitbucket]: https://bitbucket.org/

<!-- LLM API PROVIDERS -->
[anthropic]: https://docs.anthropic.com/en/home
[gemini]: https://ai.google.dev/tutorials/python_quickstart
[ollama]: https://github.com/ollama/ollama
[openai]: https://platform.openai.com/docs/quickstart/account-setup:

<!-- EXAMPLES: INPUT REPOSITORIES -->
[readme-ai]: https://github.com/eli64s/readme-ai
[pyflink]: https://github.com/eli64s/pyflink-poc
[postgres]: https://github.com/jwills/buenavista
[java]: https://github.com/avjinder/Minimal-Todo
[kotlin]: https://github.com/rumaan/file.io-Android-Client
[docker-golang]: https://github.com/olliefr/docker-gs-ping
[vercel]: https://github.com/PiyushSuthar/github-readme-quotes
[streamlit]: https://github.com/eli64s/readme-ai-streamlit
[fastapi]: https://github.com/FerrariDG/async-ml-inference
[litellm]: https://github.com/BerriAI/litellm

<!-- EXAMPLES: OUTPUT README FILES -->
[examples-directory]: https://github.com/eli64s/readme-ai/tree/main/examples
[default]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-ai.md
[ascii-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/ascii.md
[classic-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/classic.md
[compact-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/compact.md
[modern-header]: https://github.com/eli64s/readme-ai/blob/main/examples/headers/modern.md
[svg-banner]: https://github.com/eli64s/readme-ai/blob/main/examples/banners/svg-banner.md
[dalle-logo]: https://github.com/eli64s/readme-ai/blob/main/examples/logos/dalle.md
[readme-kotlin]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-kotlin.md
[for-the-badge]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-docker-go.md
[fastapi-redis]: https://github.com/eli64s/readme-ai/blob/main/examples/readme-fastapi-redis.md
[offline-mode]: https://github.com/eli64s/readme-ai/blob/main/examples/offline-mode/readme-litellm.md