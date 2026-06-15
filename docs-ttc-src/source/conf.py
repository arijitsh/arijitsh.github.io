# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Make the bundled extensions (e.g. the SMT-LIB lexer) importable.
sys.path.insert(0, os.path.abspath("_ext"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'docs-ttc'
copyright = '2026, Arijit Shaw'
author = 'Arijit Shaw'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.mathjax",
    "sphinxcontrib.bibtex",
]

# -- extension:: sphinxcontrib.bibtex ----------------------------------------

bibtex_bibfiles = ["references.bib"]
bibtex_reference_style = "label"

templates_path = ['_templates']
exclude_patterns = []

# Prefix autosectionlabel targets with the document name so that identical
# section titles (e.g. "Options") across pages do not collide.
autosectionlabel_prefix_document = True



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "navigation_depth": 5,
    "collapse_navigation": False,
}

# Logo shown in the sidebar search box (cvc5-style branding).
html_logo = "_static/ttc.png"

html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sourcelink = False

# -- SMT-LIB syntax highlighting ---------------------------------------------

from smtliblexer import SmtLibLexer
from sphinx.highlighting import lexers

lexers["smtlib"] = SmtLibLexer()