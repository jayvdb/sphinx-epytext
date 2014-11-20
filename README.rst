Sphinx epytext support
======================

sphinx-epytext provides basic support for epytext docstrings
<http://epydoc.sourceforge.net/epytext.html> 
in Sphinx autodoc <http://sphinx-doc.org/ext/autodoc.html>. 

It connects to the 'autodoc-process-docstring' hook of Sphinx, to perform the following:

- Replaces '@' with ':' for epydoc fields. <http://epydoc.sourceforge.net/fields.html>
- Replaces L{..} and C{..} with :py:obj:`..`
- Removes U{..} from around links

Configuration
-------------

Add it to your extensions in ``conf.py``::

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx_epytext',
        # your other sphinx extensions
        # ...
    ]

Then run ``sphinx-build``.
