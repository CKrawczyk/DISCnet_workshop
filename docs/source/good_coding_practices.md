# Good coding practices

## Overview: What problems do good coding practices solve?

Weather you are working alone or working in a team, one of the most valuable things you should keep in mind is **context transfer**.  It is not enough to just track the changes made to code, but to also track **why** those changes were made.  Many of the best practices covered within this document will be various flavors of recoding this kind of context in a way that is clear to other developers, or even to yourself when you look back at old code.

When context is well recorded it becomes easier for other develops to be on-boarded into your codebase, structural changes to the code become easier to manage, leading to code that is easier to maintain in the long run.

## Context transfer

Ways to boost context transfer:

- Pair programming: Work with another developer in real time when writing your code.  Typically you have one person drive the keyboard focusing on code syntax and code legibility while the other drives the code structure focusing on how the code should be structured and the algorithms being used.  Every so often these roles should switch.
- Git commit messages: Include the **why** for every change directly in the commit message
- GitHub Pull Requests: Use this space for the larger reason behind any changes and/or features
- [Architecture Decision Record](https://github.com/joelparkerhenderson/architecture-decision-record) (ADR): For larger code bases ADRs can be used to track changes to a code's architecture over time.  These records are kept in the repository next to the code and can be refereed to by and developer who wants to know the why the code is structured the way it is. 

## Code and file structure

One of the key things to keep in mind when writing code in a team is that other people will be reading and reviewing you code.  To that end it is always worth the time make the process of reading your code as easy as possible.

### Organizing your code

Step one in making your code more readable is to organize it into different files and folders.  Some rules that help with this:

- Every file has one large function, one class, or collection of related small functions
    - The file name should reflect what the code in the file does
- Group the files by the general task they complete (e.g. a folder of plotting code and a folder for analysis)
    - The folder name should reflect this general task

It is OK if you don't have a full plan for what these file and folder structures will look like before you start, you can always re-organize your code after it is written.  The important thing is to have it be at least somewhat organized before code review.  Any question you have about this structure you can alway flag up for your reviewer to take a look at and help answer.

### Code legibility

It is difficult to review code if you don't know what task the code it trying to solve.  Aside from supplying the context for your code in your PR message and/or commit message (more on that later), there are thing you can do directly in your code to help your reviewer:

- Use descriptive variable names
- Write documentation strings explaining every input and output
- Write your code in the simplest way that works
    - It should be obvious from the code written what is being done
- If you need to do something in a "clever" way write a comment about it and record in a comment, commit message, and/or PR message why this is needed
- Make sure the tone of your comments matches who you expect to be reading them
    - Comments targeted at people learning python syntax for the first time should look different than comments targeted at people who have been using python for several years
- Stick to a consistent coding style (more on this latter)
- Keep in mind your reviewer will be mostly looking at code diffs, so put some thought how you changes will look in that format.  As and example take the following code change:

```python
a = {'b': 2, 'c': 3, 'd': {'e': 5, 'f': 6}}
```
changes to 
```python
a = {'b': 1, 'c': 3, 'd': {'e': 5, 'f': 7}}
```

There are two changes made to elements of the dictionary, as written these will show up as one line of code changed.  If the line is quite long (or the reviewer is only looking at the code quickly) they might only see the first change.  To make it more obvious that multiple elements change you can format the code so every element is on its own line:

```python
a = {
    'b': 1,
    'c': 3,
    'd': {
        'e': 5, 
        'f': 7
    }
}
```

That way each element change is shown as a different line in the code diff.  As an added bonus this can help shorten long lines of code.

### Packaging code

Packaging your code will make it easier for others (including yourself) to install and use your code.  In this section I will go over how to package python code.  This workshop's repository is already setup to be a python package and can be used as a reference:

```
DISCnet_workshop (git repository)
├── data_transforms (python package base folder)
│   ├── __init__.py (needed in every folder of the package, run on folder import)
│   ├── angle_metric.py (code file)
│   └── tests (folder to hold tests)
│       ├── __init__.py
│       └── test_angle_metric.py (test file)
├── LICENSE (make sure you license your code)
├── README.md (shown on the github page)
├── setup.cfg (python package configuration)
└── setup.py (needed for back compatibility for older versions of pip)
```

Let's dive into a few of these things in more detail
- `__init__.py`: A python package treats every folder as a class with this file as the initialization function, useful for pulling functions from the files and folders inside this folder into the top level namespace.  The top level `__init__.py` typically also stores the package `__version__` variable.
- `LICENSE`: You should choose a license for your code. [Choose A License](https://choosealicense.com/) is a good resource for figuring out what license is best for your project.  The typical ones seen for research code are the [MIT license](https://choosealicense.com/licenses/mit/) and [Apache 2.0 license](https://choosealicense.com/licenses/apache-2.0/).
- `setup.cfg`: This file tells python how to install your code, what dependencies to install, and various development configuration options.

### Setting dependency versions

To help with code reproducibility and dependency compatibility you can should pin dependency versions to a single value or a range.  It is python convention that the dependencies in `setup.cfg` are pinned as **ranges** to ensure they are easy to install into existing environments and not collide with the dependencies of other packages installed.  An optional `requirements.txt` file is typically used to pin down **exact** package versions when reproducibility is more important (e.g. all developers wanting to have the same versions installed or keeping a record of the package versions installed when a paper was published using the code).

```{note}
Most python packages use [semantic versioning](https://semver.org/).  This means the version numbers are set as MAJOR.MINOR.PATCH 
- MAJOR version increments when incompatible API changes are made to the code
- MINOR version increments when a new feature is added in a backward compatible manner
- PATCH version increments when a backward compatible bug fix is made
```

The rule of thumb I use when pinning down my packages ranges in `setup.cfg`:
- Set the lower bound as `>=` the exact version currently installed in my environment (use `conda list` or `pip freeze` to view the current versions of installed packages)
- Set the upper bound as `<` the next patch fix version of the package
- Activate [dependabot](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/) on GitHub to automatically make pull requests that update the upper bound when dependencies update (as we will see in the next section this will trigger our tests to run automatically and let us know if the update breaks the code)
    - If a dependency update breaks the code (typically major version updates), update the code and set the lower bound to be the latest version of the dependency

### Versioning your package

It is a good idea to use single-source package versioning, this means the package version is defined in exactly one place inside the repository.  For python this is typically inside the top level `__init__.py` file and stored with the variable name `__version__`.  The `setup.cfg` file can read this version by using:

```
[metadata]
version = attr: data_transforms.__version__
```

where `data_transforms` is the name of the python package we are writing in this workshop.

When you are ready to release a new version of your code make a new PR that only bumps the version number using semantic versioning (see note above).  Once merged add a git tag to the merge commit.  You can also add additional notes about the release when making the tag, this a good place to include what things have changed in the new release.

For larger projects it is worth keeping a separate `CHANGELOG.md` file inside the repository or a changelog section in the `README.md` that tracks all the changes introduced in each version bump to make this information easier to find.  There are tools available to help automate this process, these typically involve using special keywords when writing git commit messages to flag up text related to new features and/or breaking changes (e.g. [auto-changelog](https://github.com/KeNaCo/auto-changelog)).

## Text editors

Although there are numerous IDEs (e.g. IDLE, Spyder) for python, for most everyday use you will likely be writing python code in a text editor and running your programs via the command line.  In this case it is important to have a good text editor that supports syntax highlighting, live linting (syntax and style checking), and is easy to configure the way you want.  I can highly recommend [VScode](https://code.visualstudio.com/) as a free quality text editor with all the features above.

For python coding you will want to install the `Python` extension by Microsoft (you will be prompted to install it when you first open a `.py` file) and the `Jupyter` extension by Microsoft.  

### Programming fonts

In addition to a good text editor you will also want a good monospace font.  I can recommend [FiraCode](https://github.com/tonsky/FiraCode).  This font has ligatures (special characters used represent specific letters that appear next to each other) that help when reading code (e.g. turing `>=` int a "less-than or equal" to sign).  As this can be a bit annoying while typing, you can also use the VScode `Disable Ligatures` extension to turn this feature off for the active line you are typing.  Once the font and extension are installed you will need to edit VScode's `settings.json` file with the options (all other font options can be set from the normal settings panel):

```json
{
    "editor.fontFamily": "Fira Code",
    "editor.fontLigatures": true,
    "editor.fontWeight": "500",
    "disableLigatures.mode": "Line",
}
```

## Coding style and linting

What is a coding style?  Beyond the syntax of a coding language, a coding style is a set of conventions that can be followed to make it easier for other developers (including your future self) to read you code and to understand the intention behind your code.  For python coding the style most developers use has it basis in [PEP 8](https://peps.python.org/pep-0008/).

Here are some examples of PEP 8 conventions:

- Use 4 spaces to indent lines (rather than a tab)
- A max line limit of 79 characters (preferred by people who use command line editors, I typically override this to be higher)
- Constants are defined at the module level with names in ALL_CAPS
- Class names should normally use the CapWords convention
- Function names should be lowercase, with words separated by underscores as necessary to improve readability

As PEP 8 is so common across python there are packages you can install that will automatically check you style for you (and text editors that will do this as you type).  The two most common ones used are [pylint](https://pylint.pycqa.org/en/latest/) and [flake8](https://flake8.pycqa.org/en/latest/).  While both cover the standard PEP 8 rules, they each have a different set of additional style rules that are checked (e.g. variables that are defined but not used).  Of the two `flake8` is a bit less opinionated making it a bit easier to get on with, because of this we will be using it for the workshop. Once `flake8` is install you can run it on the command line with:

```bash
flake8
```

in the top level folder with your code and it will check the style in every python file.  This process of checking the style of you code is called "linting."

### Configuring your linter

While `flake8` is a great starting point, it is just that, a starting point.  PEP 8 should be used as a guideline for your projects style and if there are any rules you don't agree with you are free to turn them off.  While this can be configured globally on your local computer, I would recommend doing at the project level inside your code's `setup.cfg` file.  By doing it at the project level your choice of style rules will be saved **inside the project** for all developers to see.  That way everyone contributing code to the project knows what rules to follow (and what ones can be ignored).

In particular, withing `flake8` rules [W503](https://www.flake8rules.com/rules/W503.html) and [W504](https://www.flake8rules.com/rules/W504.html) are the exact opposite of each other, so one of them must be ignored.  Within this project I have already set up the `flake8` configuration in the `setup.cfg` file to:

- ignore the project configuration folders (.git, docs, etc...)
- Set the max line length to 120
- Turn off rule `W503`
- Turn off `BLK100` (flake-black, black is an optional set of rules we are not going to be using)

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

### Sphinx - building the docs

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

