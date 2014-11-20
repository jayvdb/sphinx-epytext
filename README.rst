Sphinx epytext support
======================

sphinx-epytext provides basic support for epytext docstrings <http://epydoc.sourceforge.net/epytext.html> in Sphinx autodoc <http://sphinx-doc.org/ext/autodoc.html>. 

- Replaces '@' in docstrings with ':' for epydoc fields. <http://epydoc.sourceforge.net/fields.html>
- Replaces L{..} and C{..} with :py:obj:`..`
- Removes U{..} from around links

To use it, add 'sphinx_epytext' to 'extensions' in your Sphinx conf.py and run sphinx-build.
