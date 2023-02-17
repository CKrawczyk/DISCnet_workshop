# Packaging Python code
This section of notes is partially adapted from [https://github.com/cameron-simpson/css/blob/pypi/doc/pypa-the-missing-outline.md](https://github.com/cameron-simpson/css/blob/pypi/doc/pypa-the-missing-outline.md)

A python package is the process of collecting your code in a way that can be installed on a different person's computer.  This process is made up of several parts:

- The source code
- A configuration file with the package's metadata (a `pyproject.toml` file)
- Build artifacts that are uploaded to a package distribution service such as [PyPI](https://pypi.org/).  These are typically a source distribution (sdist) and a built distribution (wheel).

## The build system
To build your package you will need to pick a build system.  There are no build systems that come with python by default.  In the past `setuptools` was the defacto standard, but in recent years more have become available.  For this workshop we will be using [flit](https://flit.pypa.io/en/latest/) as it is lightweight and compliant with the latest python standards.

A build system typically comes with a command line interface (CLI) that can automate common tasks such as making a new python environment with you code installed, bumping your code's version number, building the `sdist` and `wheel`s, or uploading the builds to PyPI.

Common build systems are:
- [flit](https://flit.pypa.io/en/latest/): just a build system, nothing more
- [hatch](https://hatch.pypa.io/latest/): build system and environment management
- [pdm](https://pdm.fming.dev/latest/): build system, dependency management, dependency locking, and environment management (note: the environments are handled in the background so you don't have to do it by hand)
- [poetry](https://python-poetry.org/docs): build system, dependency management, dependency locking, and environment management (note: not [PEP 621](https://peps.python.org/pep-0621/) compliant, but it is on their long-term [feature road map](https://github.com/python-poetry/roadmap/issues/3))

Each of these build systems have different workflows when managing your python package, it can be useful to try some of them out and see what one fits your project best.

```{note}
Python's packaging landscape is currently (Summer 2022) in flux.  You will find many out of date tutorials around making a `setup.py` and/or `setup.cfg` instead of/in addition to the `pyproject.toml`.  As of [PEP 621](https://peps.python.org/pep-0621/) (approved in 2021), the method outlined in these notes is the "approved python" way of making a package going forward.  As of `pip` version 22.1.2 this new way of packaging is fully supported. 
```

## The source code structure
This workshop's repository is already setup to be a python package let's take a closer look at the structure.  The minimum files for this workshop's code are:

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
└── pyproject.toml (contains package metadata and dependencies)
```

- `__init__.py`: A python package treats every folder as a class with this file as the initialization function, useful for pulling functions from the files and folders inside this folder into the top level namespace.  The top level `__init__.py` typically also stores the package `__version__` variable.
- `LICENSE`: You should choose a license for your code. [Choose A License](https://choosealicense.com/) is a good resource for figuring out what license is best for your project.  The typical ones seen for research code are the [MIT license](https://choosealicense.com/licenses/mit/) and [Apache 2.0 license](https://choosealicense.com/licenses/apache-2.0/).
- `pyproject.toml`: This file tells python how to install your code, what dependencies to install, and various development configuration options.  You can use `flit init` to help build this file or just write it by hand.

## Setting dependency versions
To help with code reproducibility and dependency compatibility you can should pin dependency versions to a single value or a range.  It is python convention that the dependencies in `pyproject.toml` are unpinned or pinned as **ranges** to ensure they are easy to install into existing environments and not collide with the dependencies of other packages installed.  An optional file (either `requirements.txt` or the lock file created by your build tool) is used to pin down **exact** package versions when reproducibility is important (e.g. all the developers wanting to have the same versions of dependencies installed, keeping a record of the package versions installed when a paper was published using the code, or ensuring web apps deploy with the same versions the tests ran with).

```{note}
Most python packages use [semantic versioning](https://semver.org/).  This means the version numbers are set as MAJOR.MINOR.PATCH 
- MAJOR version increments when incompatible API changes are made to the code
- MINOR version increments when a new feature is added in a backward compatible manner
- PATCH version increments when a backward compatible bug fix is made
```

The rule of thumb I use when pinning down my packages ranges:
- Set the lower bound as `>=` the exact version currently installed in my environment (use `conda list` or `pip freeze` to view the current versions of installed packages)
- Set the upper bound as `<` the next patch fix version of the package
- Activate [dependabot](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/) on GitHub to automatically make pull requests that update the upper bound when dependencies update (this will trigger our CI to run our tests automatically and let us know if the update breaks the code)
    - If a dependency update breaks the code (typically major version updates), update the code and set the lower bound to be the latest version of the dependency

## Installing your package locally
When you install a python package it will typically involve copying the python files to your `site-packages` directory.  Running `pip install .[dev]` in the top level directory (same folder as the `pyproject.toml` file) will do just this.  If you are actively developing your code and want to test out your latest changes you would need to reinstall the code with every change, this can become tedious.

To help developers, `pip` also has the ability to install a package in "edit" mode, this creates a symbolic link in `site-packages` that points to your source code, that way change can be seen without needing to reinstall the code.

```bash
pip install -e .[dev]
```

## Versioning your package
It is a good idea to use single-source package versioning, this means the package version is defined in exactly one place inside the repository.  For python this is typically inside the top level `__init__.py` file and stored with the variable name `__version__`.  `flit` will automatically pull the version number from this place and use it in the `pyporject.toml` file (this is why "version" is listed in the `dynamic` section)

When you are ready to release a new version of your code make a new PR that only bumps the version number using semantic versioning (see note above).  Once merged add a git tag to the merge commit.  You can also add additional notes about the release when making the tag, this a good place to include what things have changed in the new release.

For larger projects it is worth keeping a separate `CHANGELOG.md` file inside the repository or a changelog section in the `README.md` that tracks all the changes introduced in each version bump to make this information easier to find.  There are tools available to help automate this process, these typically involve using special keywords when writing git commit messages to flag up text related to new features and/or breaking changes (e.g. [auto-changelog](https://github.com/KeNaCo/auto-changelog)).

## Build artifacts
If/when you are ready to upload your files to `PyPI` you first need to crete the files that will be uploaded.  These can be done with our chosen build tool:

```bash
flit build
```

This will create two files in the `dist` subdirectory:

- `data_transforms-0.1.0.tar.gz`: this is the `sdist` file, a normal zip folder with the source code inside
- `data_transforms-0.1.0-py3-none-any.whl`: this is the `wheel` file, also a zip folder with the pre-compiled code inside (if you code is pure python it will be basically identical to the `sdist`s contents)

The code version number is automatically used in the build names, this prevents older code version from being overwritten when the version is updated.

## Build upload
To publish your package to [PyPI](https://pypi.org/) you will first need to create an account.  Once created you can use your build tool or [twine](https://twine.readthedocs.io/en/stable/) to upload your build artifacts.  For uploading with `flit` see their docs [https://flit.pypa.io/en/latest/upload.html](https://flit.pypa.io/en/latest/upload.html).

```{note}
The build and upload systems can be written into a GHA that triggers when a new version is tagged so you never forget the step of releasing your code to the public.
```
