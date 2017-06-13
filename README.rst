sphinx-autodoc-pywps
====================

*Use Process class magic in sphinx-enabled docstrings*


Installation
------------

First, you need pywps-based processes and a Sphinx documentation (with ``autodoc`` enabled).

You can install ``sphinx-autodoc-pywps`` with::

    $ pip install sphinx-autodoc-pywps

Then, you need to enable it in your ``conf.py`` file::

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx_autodoc_pywps',
    ]

You're done!

Usage
-----

