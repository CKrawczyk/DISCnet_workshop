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
