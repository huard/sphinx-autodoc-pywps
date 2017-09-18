from setuptools import setup

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Operating System :: OS Independent',
    'Topic :: Documentation',
]

setup(
    name = "sphinx-autodoc-pywps",
    version = "0.1",
    #url = "https://github.com/hsoft/sphinx-autodoc-annotation",
    py_modules = ['sphinx_autodoc_pywps'],
    install_requires = [
        'sphinx>=1.3',
    ],
    author="David Huard",
    author_email="david.huard@gmail.com",
    description="Use pywps Process tricks in sphinx-enabled docstrings",
    long_description=open('README.rst', 'rt').read(),
    license="BSD",
    classifiers=CLASSIFIERS,
)
