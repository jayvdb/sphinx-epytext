# -*- coding: utf-8 -*-
"""Process docstrings."""

import re

FIELDS = [
    'param',
    'keyword',
    'kwarg',
    'type',
    'returns',
    'return',
    'rtype',
    'raises',
    'exception',
    'see',
    'note',
    # not tested
    'attention',
    'bug',
    'warning',
    'version',
    'todo',
    'deprecated',
    'since',
    'status',
    'change',
    'permission',
    'requires',
    'precondition',
    'postcondition',
    'invariant',
    'author',
    'organization',
    'copyright',
    'license',
    'contact',
    'summary',
]

# Not supported yet: 'group', 'sort'


def process_docstring(app, what, name, obj, options, lines):
    """
    Process the docstring for a given python object.

    Note that the list 'lines' is changed in this function. Sphinx
    uses the altered content of the list.
    """
    result = [re.sub(r'U\{([^}]*)\}', r'\1',
                     re.sub(r'(L|C)\{([^}]*)\}', r':py:obj:`\2`',
                            re.sub(r'@(' + '|'.join(FIELDS) + r')', r':\1',
                                   l)))
              for l in lines]
    lines[:] = result[:]
