# Documenting Python code
When someone unfamiliar with your code first wants to use your code, the first place they will look is you documentation.  It is good practice for your documentation to start with a brief description of what your package does (1-2 paragraphs) and clear instructions for how to install the code.

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

In addition to the API documentation from the docstrings you should also provide tutorials on how to use you code (python notebooks work great for this kind of documentation).  You can also provide additional information in markdown format (like these notes you are reading now).

## Sphinx
Once you have written your docs you need a way to collect all of it into a single place, typically a web site.  The most common way to do this in python is to use the [Sphinx](https://www.sphinx-doc.org/en/master/index.html) package.  The setup for Sphinx can be a bit involved, but once set up it "just works."

### Config
Sphinx has already been set up on this project, but while I was doing it I took notes about every step.  To setup Sphinx on this project I used the following commands:

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
import sys
sys.path.insert(0, os.path.abspath('../..'))
```

Tell Sphinx what extensions to use:
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

And change the theme:
```python
html_theme = 'sphinx_rtd_theme'
```

### API documentation with `apidoc`
For Sphinx to be able to read the docstrings from your source code it first needs be told what source files to look in.  This can either be done by adding your source folders by hand to `docs/soruce/index.rst` or by using the `sphinx-apidoc` command to build these `.rst` files for you.  We will be using this automated approach for this workshop:

```bash
sphinx-apidoc -MEf -o ./docs/source ./data_transforms ./data_transforms/tests
```

What is this command doing:
 - `-M`: put module documentation before submodule documentation
 - `-E`: don't create headings for the modules or packages (e.g. when the docstrings already contain them)
 - `-f`: overwrite existing files
 - `-o ./docs/source`: the output directory
 - `./data_transforms`: the package directory
 - `./data_transforms/tests`: directories to exclude

This command will create two files: `data_transforms.rst` and `modules.rst`. While I think the templates used for these files are not the best in the world, they can provide a good starting place for learning what these files should look like.  

```{note}
There are also options for customizing these templates, but that is outside the scope of this workshop.
```

As we will be running this command every time the docs are built (to check for new code files) the resulting `rst` files have been added to the `.gitignore` file.

Lastly we need to update the `index.rst` file to include the files create with this command (and these class notes while we are at it):

```rst
DISCnet Workshop: Writing Code as a Team
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Setting the Stage

   introduction
   the_task

.. toctree::
   :maxdepth: 2
   :caption: Workshop Notes:

   getting_started
   good_coding_practices
   github_with_collaborators
   code_structure
   packaging_python_code
   writing_documentation
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

### Building the docs
With the `rst` files inplace, we can build the docs with:

```bash
cd docs
make html
```

This will create the static HTML files in the `docs/build/html` folder.  You can open `docs/build/html/index.html` in your favorite browser and see the results.

```{note}
Sometimes the side bar content will not update correctly when new pages are added, to fix this run `make clean` before `make html` to remove cached data.
```

To simplify the auto finding and doc building steps I have created a `build_docs.sh` script in the base repository to run all the commands above in order:

```bash
cd docs
sphinx-apidoc -MEf -o ./source ../data_transforms ../data_transforms/tests
make clean
make html
cd ..
```
