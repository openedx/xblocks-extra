"""
Sphinx configuration for xblocks-extra documentation.
"""

import os
import sys
from datetime import datetime

# Add the project root to the path for autodoc
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "xblocks-extra"
copyright = f"{datetime.now().year}, Axim Collaborative, Inc."
author = "Axim Collaborative, Inc."

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_book_theme"

html_theme_options = {
    "repository_url": "https://github.com/openedx/xblocks-extra",
    "repository_branch": "main",
    "path_to_docs": "docs/",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "home_page_in_toc": True,
    "extra_footer": """
        <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">
            <img
                alt="Creative Commons License"
                style="border-width:0"
                src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png"/>
        </a>
        <br>
        These works by
            <a
                xmlns:cc="https://creativecommons.org/ns#"
                href="https://openedx.org"
                property="cc:attributionName"
                rel="cc:attributionURL"
            >Axim Collaborative, Inc</a>
        are licensed under a
            <a
                rel="license"
                href="https://creativecommons.org/licenses/by-sa/4.0/"
            >Creative Commons Attribution-ShareAlike 4.0 International License</a>.
    """,
}

html_logo = "https://logos.openedx.org/open-edx-logo-color.png"
html_favicon = "https://logos.openedx.org/open-edx-favicon.ico"

# -- Options for intersphinx -------------------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.12", None),
    "django": ("https://docs.djangoproject.com/en/4.2/", "https://docs.djangoproject.com/en/4.2/_objects/"),
}
