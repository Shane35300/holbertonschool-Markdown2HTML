#!/usr/bin/python3
""" This module check if the Markdoxn exist and display an error message
"""

import sys
import os


def convert_markdown_to_html(markdown_file, output_file):
    """
    Check if the Markdown file exists and display an error message
    """
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    # Extract arguments
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML
    convert_markdown_to_html(markdown_file, output_file)

    # Exit with success
    sys.exit(0)
