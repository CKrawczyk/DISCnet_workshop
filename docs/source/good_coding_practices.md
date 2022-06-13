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

## Text editors

Although there are numerous IDEs (e.g. IDLE, Spyder) for python, for most everyday use you will likely be writing python code in a text editor and running your programs via the command line.  In this case it is important to have a good text editor that supports syntax highlighting, live linting (syntax and style checking), and is easy to configure the way you want.  I can highly recommend [VScode](https://code.visualstudio.com/) as a free quality text editor with all the features above.

For python coding in VScode you will want to install the `Python` extension by Microsoft (you will be prompted to install it when you first open a `.py` file) and the `Jupyter` extension by Microsoft.  Other useful extensions are the `Excel Viewer` extension for easier viewing CSV files, `open in browser` for and option to open HTML files in your browser, and `Code Spell Checker` for basic spell checking.

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
