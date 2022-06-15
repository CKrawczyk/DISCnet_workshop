# Documenting Python code

When someone unfamiliar with your code first wants to use it the first place they will look is you documentation.  It is good practice for your documentation to start with a brief description of what your package does (1-2 paragraphs) and clear instructions for how to install the code.

To help ensure that the source code and the documentation don't get out of sync, the documentation for each function should be included as a docstring on the function in the source code.  In python this is done with a "triple quote string":

```python
def sum_two_numbers(a, b):
    '''Return the sum of the two inputs'''
    return a + b
```

Or a more explicit docstring (using [numpy's style guide](https://numpydoc.readthedocs.io/en/latest/format.html#style-guide)):

```python
def sum_two_numbers(a, b):
    '''Return the sum of the two inputs

    Parameters
    ----------
    a : float
        The first value in the sum
    b : float
        The second value in the sum

    Returns
    -------
    float
        The sum of `a` and `b`
    '''
    return a + b
```

## Sphinx - config
In addition to the API documentation from the docstrings you can also provide tutorials on how to use you code (python notebooks work great for this kind of documentation).

Once you have written your docs you need a way to collect all of it into a single place, typically a web site.  The more common way to do this in python is to use the [Sphinx](https://www.sphinx-doc.org/en/master/index.html) package.  The setup for Sphinx can be a bit involved, but once set up it "just works."

To setup Sphinx on this project I used the following commands:

```bash
pip install sphinx, myst-nb, sphinx_rtd_theme

cd DISCnet_workshop
mkdir docs
cd docs
sphinx-quickstart
```

with the following options:
- Separate source and build directories (y/n) [n]: y
- Project name: Data Transforms
- Author name(s): Coleman Krawczyk
- Project release []: 0.1.0
- Project language [en]: en

The final part the setup is adjusting the `docs/source/conf.py` file to tell it where our source package lives:

```python
import os
import sphinx_rtd_theme
import sys
sys.path.insert(0, os.path.abspath('../..'))
```

```python
extensions = [
    'sphinx.ext.autodoc',  # auto find doc strings in source code
    'sphinx.ext.napoleon',  # numpy style docstrings
    'sphinx_rtd_theme',  # Read the Docs theme
    'myst_nb'  # markdown and notebook support
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst-nb',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
    '.txt': 'myst-nb'
}

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store'
]
```

Change the theme:

```python
html_theme = 'sphinx_rtd_theme'
```

## Sphinx - apidoc

For sphinx to be able to read the docstrings from your source code it first needs be told what source files to look in.  This can either be done by adding your source folders by hand to `docs/soruce/index.rst` or by using the `sphinx-apidoc` command to build these `.rst` files for you.  We will be using this automated approach for this workshop:

```bash
sphinx-apidoc -MEf -o ./docs/source ./data_transforms ./data_transforms/tests
```

What is this command doing:
 - `-M`: put module documentation before submodule documentation
 - `-E`: don't create headings for the module/package packages (e.g. when the docstrings already contain them)
 - `-f`: overwrite existing files
 - `-o ./docs/source`: the output directory
 - `./data_transforms`: the package directory
 - `./data_transforms/tests`: directories to exclude

While I think the templates used by this command are not the best in the world, they can provide a good starting place for learning what these files should look like.

As we will be running this command every time the docs are built (to check for new code files) the resulting `rst` files have been added to the `.gitignore` file.

Lastly we need to update the `index.rst` file to include the files create with this command (and these class notes while we are at it):

```rst
Welcome to Data Transforms's documentation!
===========================================

.. toctree::
   :maxdepth: 2
   :caption: Workshop Notes:

   Introduction
   getting_started
   good_coding_practices
   GitHub_with_collaborators
   test_driven_development

.. toctree::
   :maxdepth: 2
   :caption: API Documentation:
   
   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
```

## Sphinx - building the docs

With the `rst` files inplace, we can build the docs with:

```bash
cd docs
make html
```

This will create the static HTML files in the `docs/build/html` folder.  You can open `docs/build/html/index.html` in your favorite browser and see the results.

```{note}
Sometimes the side bar content will not update correctly when new pages are added, to fix this run `make clean` before `make html` to remove cached data.
```

To simplify the auto finding and doc building steps I have created a `build_docs.sh` script in the base repository to run the commands above in order.

