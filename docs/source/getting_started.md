# Getting started

## Making a clean python environment
When starting a new python project it is useful to create a new python environment to avoid any conflicting dependencies between projects.  Depending on how python was installed on your system this can be done in a few different ways.

### Using `venv`
Python comes with its own environment manager called `venv`.  To make a new environment named `discnet_env` run:

```bash
python3.10 -m venv discnet_env
```

This will make a new folder called `discnet_env` in the directory where you run the command.  This directory contains the python environment.

```{note}
This will make an environment using the same version of python used to run the command.  By using `python3.10` we ensure it will be a python 3.10 environment.
```

To activate the environment run (from the same directory as the previous command):

```bash
source discnet_env/bin/activate
```

### Using `conda`
If you installed python using [conda](https://docs.conda.io/en/latest/) you should use it as your environment manager.  To make a new environment named `discnet_env` run:

```bash
conda create --name discnet_env python=3.10
```

This will make a new directory called `discnet_env` inside your conda install's `envs` folder (typically in your home folder). This directory contains the python environment.

```{note}
Unlike `venv` you can specify any version of python when making an environment even if that version is not currently installed on your system.
```

To activate the environment run:

```bash
conda activate discnet_env
```

## Clone the repository
Use git to clone the repository for this workshop:

```bash
git clone https://github.com/CKrawczyk/DISCnet_workshop.git
cd DISCnet_workshop
```

## Installing the workshop's python package
Throughout this workshop you will be helping to write a python package called `data_transforms`.  To install it into your new environment (once the env is activated) run:

```bash
# make sure `pip` is up to date and install the `flit` build tool
pip install -U pip flit

# install the development version of the `data_transforms` package
pip install -e .[dev]
```

The option `-e` installs the code in "edit" mode, this means the package directory is sym-linked into your python path.  Any changes you make to the code will automatically be "installed" without needing to run the `pip` command again.  `.[dev]` indicates you want to install the python package located in the current folder and to also install the optional development dependencies for the package.  We will cover these topics in more detail in the "packaging python code" section of the workshop.

## Running tests
The notes on test driven development will go into this in more detail, but for completeness you can run this codes tests with the command:

```bash
coverage run
```

and view the test coverage report with:

```bash
coverage report
```
