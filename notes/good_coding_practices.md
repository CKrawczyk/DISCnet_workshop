# Good coding practices

## Overview: What problems do good coding practices solve?

Weather you are working alone or working in a team, one of the most valuable things you should keep in mind is **context transfer**.  It is not enough to just track the changes made to code, but to also track **why** those changes were made.  Many of the best practices covered within this document will be various flavors of recoding this kind of context in a way that is clear to other developers, or even to yourself when you look back at old code.

When context is well recorded it becomes easier for other develops to be on-boarded into your codebase, structural changes to the code become easier to manage, leading to code that is easier to maintain in the long run.

## Coding style

What is a coding style?  Beyond the syntax of a coding language, a coding style is a set of conventions that can be followed to make it easier for other developers (including your future self) to read you code and to understand the intention behind your code.  For python coding the style most developers use has it basis in [PEP 8](https://peps.python.org/pep-0008/).

Here are some examples of PEP 8 conventions:

- Use 4 spaces to indent lines (rather than a tab)
- A max line limit of 79 characters (preferred by people who use command line editors, I typically override this to be higher)
- Constants are defined at the module level with names in ALL_CAPS
- Class names should normally use the CapWords convention
- Function names should be lowercase, with words separated by underscores as necessary to improve readability

As PEP 8 is so common across python there are packages you can install that will automatically check you style for you (and text editors that will do this as you type).  The most common package is [flake8](https://flake8.pycqa.org/en/latest/), once install you can run:

```bash
flake8
```

in the top level folder with you code and it will check the style in every python file.  This process of checking the style of you code is called "linting."

### Configuring your linter

While PEP 8 is a great starting point, it is just that, a starting point.  PEP 8 should be used as a guideline for your projects style and if there are any rules you don't agree with you are free to turn them off.  While this can be configured globally on your local computer, I would recommend doing at the project level inside your code's `setup.cfg` file.  By doing it at the project level your choice of style rules will be saved **inside the project** for all developers to see.  That way everyone contributing code to the project knows what rules to follow (and what ones can be ignored).

In particular, withing `flake8` rules [W503](https://www.flake8rules.com/rules/W503.html) and [W504](https://www.flake8rules.com/rules/W504.html) are the exact opposite of each other, so one of them must be ignored.  Within this project I have already set up the `flake8` configuration in the `setup.cfg` file to:

- ignore the `.git` and `__pycache__` folders
- Set the max line length to 120
- Turn off rule `W503`
- Turn off `BLK100` (flake-black)

## Documenting code

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

### Sphinx - config
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
sys.path.insert(0, os.path.abspath('..'))
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

### Sphinx - apidoc

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

### Sphinx - building the docs

With the `rst` files inplace, we can build the docs with:

```bash
cd docs
make html
```

This will create the static HTML files in the `docs/build/html` folder.  You can open `docs/build/html/index.html` in your favorite browser and see the results.

To simplify the auto finding and doc building steps I have created a `build_docs.sh` script in the base repository to run the commands above in order.

## Code (file) structure
Writing code in a way that makes it easier to review
Packaging code

## Text editors
Live linting
Syntax highlighting
Programming fonts (e.g. https://github.com/tonsky/FiraCode)

## Context transfer
Pair programming
Code review (will tie into GitHub)
Code commenting
Documentation
