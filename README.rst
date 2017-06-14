sphinx-autodoc-pywps
====================

*Automatically generate documentation for pywps Process subclasses in 
sphinx*

Installation
------------

First, you need pywps-based processes and a Sphinx documentation (with ``autodoc`` enabled).

You can install ``sphinx-autodoc-pywps`` with::

    $ git clone git@github.com:huard/sphinx-autodoc-pywps.git
    $ cd sphinx-autodoc-pywps
    $ python setup.py install

Then, you need to enable the extension in your ``conf.py`` file, along
with the `napoleon`_ extension and set the ``napoleon_numpy_docstring``
flag to ``True``::

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon'
        'sphinx_autodoc_pywps',
    ]
    
    napoleon_numpy_docstring = True

The `numpy docstring`_ convention is used because it is the only one at the
moment supporting multiple outputs. 

Usage
-----

Simply use the ``autoclass`` directive with `pywps`_ Process subclasses
in your documentation::

    .. autoclass:: flyingpigeon.processes.IndicespercentileProcess

This will parse the ``Process`` instance for its identifier, title, 
abstract, version, inputs & outputs as well as metadata. Additional 
documentation sections can be added in the class docstring itself, and 
will be appended to the class documentation. 


Testing
-------

Install `flyingpigeon`_, then go into the ``docs`` directory and run ``make html``. This will build a simple documentation for a few flyingpigeon processes. 

.. _napoleon: https://sphinxcontrib-napoleon.readthedocs.io
.. _numpy docstring: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt 
.. _pywps: http://pywps.org/
.. _flyingpigeon: https://github.com/bird-house/flyingpigeon
