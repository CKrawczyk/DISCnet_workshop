# Packaging Python code

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

## The package structure

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
