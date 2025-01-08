import re
from pathlib import Path
from typing import Dict, List, Tuple

content = """
# Pydantic
[![CI](https://img.shields.io/github/actions/workflow/status/pydantic/pydantic/ci.yml?branch=main&logo=github&label=CI)](https://github.com/pydantic/pydantic/actions?query=event%3Apush+branch%3Amain+workflow%3ACI)
[![Coverage](https://coverage-badge.samuelcolvin.workers.dev/pydantic/pydantic.svg)](https://coverage-badge.samuelcolvin.workers.dev/redirect/pydantic/pydantic)
[![pypi](https://img.shields.io/pypi/v/pydantic.svg)](https://pypi.python.org/pypi/pydantic)
[![CondaForge](https://img.shields.io/conda/v/conda-forge/pydantic.svg)](https://anaconda.org/conda-forge/pydantic)
[![downloads](https://static.pepy.tech/badge/pydantic/month)](https://pepy.tech/project/pydantic)
[![versions](https://img.shields.io/pypi/pyversions/pydantic.svg)](https://github.com/pydantic/pydantic)
[![license](https://img.shields.io/github/license/pydantic/pydantic.svg)](https://github.com/pydantic/pydantic/blob/main/LICENSE)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://docs.pydantic.dev/latest/contributing/#badges)

Data validation using Python type hints.

Fast and extensible, Pydantic plays nicely with your linters/IDE/brain.
Define how data should be in pure, canonical Python 3.8+; validate it with Pydantic.

## Pydantic Logfire :fire:

We've recently launched Pydantic Logfire to help you monitor your applications. [Learn more](https://pydantic.dev/articles/logfire-announcement)

## Pydantic V1.10 vs. V2

Pydantic V2 is a ground-up rewrite that offers many new features, performance improvements, and some breaking changes compared to Pydantic V1.

If you're using Pydantic V1 you may want to look at the [pydantic V1.10 Documentation](https://docs.pydantic.dev/) or, [`1.10.X-fixes` git branch](https://github.com/pydantic/pydantic/tree/1.10.X-fixes). Pydantic V2 also ships with the latest version of Pydantic V1 built in so that you can incrementally upgrade your code base and projects: `from pydantic import v1 as pydantic_v1`.

## Help

See [documentation](https://docs.pydantic.dev/) for more details.

## Installation

Install using `pip install -U pydantic` or `conda install pydantic -c conda-forge`.
For more installation options to make Pydantic even faster,
see the [Install](https://docs.pydantic.dev/install/) section in the documentation.

## A Simple Example

```python
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {'id': '123', 'signup_ts': '2017-06-01 12:22', 'friends': [1, '2', b'3']}
user = User(**external_data)
print(user)
#> User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
#> 123
```

## Contributing

For guidance on setting up a development environment and how to make a
contribution to Pydantic, see [Contributing to Pydantic](https://docs.pydantic.dev/contributing/).

## Reporting a Security Vulnerability

See our [security policy](https://github.com/pydantic/pydantic/security/policy).
"""


class MarkdownRefLinksConverter:
    def __init__(self):
        # Regular expression for finding Markdown links, including image links
        self.link_pattern = r"\[([^\]]+)\]\(([^\)]+)\)"

    def extract_links(self, content: str) -> List[Tuple[str, str, str]]:
        """
        Extract all markdown links from the content.
        Returns a list of tuples: (original_text, text, url)
        """
        matches = re.finditer(self.link_pattern, content)
        return [(match.group(0), match.group(1), match.group(2)) for match in matches]

    def generate_reference_id(self, text: str, used_refs: Dict[str, str]) -> str:
        """
        Generate a unique reference ID based on the link text.
        Handles duplicates by adding numbers.
        """
        # Remove any leading ! for image links
        text = text.lstrip("!")

        # Create a basic reference from the text
        ref = re.sub(r"[^\w\s-]", "", text.lower())
        ref = re.sub(r"[-\s]+", "-", ref).strip("-")

        # If empty or only special characters, use 'link'
        if not ref:
            ref = "link"

        # Handle duplicates
        base_ref = ref
        counter = 1
        while ref in used_refs and used_refs[ref] != text:
            ref = f"{base_ref}-{counter}"
            counter += 1

        return ref

    def convert_to_reflinks(self, content: str) -> str:
        """
        Convert all regular Markdown links to reference-style links.
        Returns the modified content with references.
        """
        links = self.extract_links(content)
        if not links:
            return content

        references = {}
        used_refs = {}
        modified_content = content

        # Add separator and comment before reference section
        reference_section = "\n\n---\n\n<!-- REFERENCE LINKS -->\n"

        for original, text, url in links:
            ref_id = self.generate_reference_id(text, used_refs)
            used_refs[ref_id] = text
            references[ref_id] = url

            is_image = text.startswith("!")
            if is_image:
                ref_link = f"![{text[1:]}][{ref_id}]"
            else:
                ref_link = f"[{text}][{ref_id}]"

            modified_content = modified_content.replace(original, ref_link)
            reference_section += f"[{ref_id}]: {url}\n"

        return modified_content + reference_section

    def process_content(self, content: str) -> str:
        """
        Process markdown content directly and return the modified content.
        """
        return self.convert_to_reflinks(content)

    def process_file(self, input_path: str | Path, output_path: str | Path) -> None:
        """
        Process a markdown file and optionally save to a new file.
        If no output path is provided, modifies the input file in place.
        """
        input_path = Path(input_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        content = input_path.read_text(encoding="utf-8")
        modified_content = self.convert_to_reflinks(content)

        output_path = Path(output_path) if output_path else input_path
        output_path.write_text(modified_content, encoding="utf-8")


def main():
    converter = MarkdownRefLinksConverter()
    result = converter.process_content(content)
    print(result)
    output_path = "readme-with-reflinks.md"
    Path(output_path).write_text(result, encoding="utf-8")


if __name__ == "__main__":
    main()
