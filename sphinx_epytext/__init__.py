# -*- coding: utf-8 -*-
# Copyright 2014-5 John Vandenberg
# Licensed under the MIT License, see LICENSE file for details.

"""Sphinx epytext support."""

from sphinx.application import Sphinx

from sphinx_epytext.process_docstring import process_docstring


def setup(app):
    """Sphinx extension setup function.

    When the extension is loaded, Sphinx imports this module and executes
    the ``setup()`` function, which in turn notifies Sphinx of everything
    the extension offers.
    """
    if not isinstance(app, Sphinx):
        return  # probably called by tests

    app.connect('autodoc-process-docstring', process_docstring)
