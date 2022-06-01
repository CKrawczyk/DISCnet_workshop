# Using GitHub with collaborators 

## Overview: What problem is Git designed to solve?

## Basic concepts
Local repository
Remote repository
Pull from remote
Push to remote
Commit
Branch

## Writing good commit messages

These notes are partially adapted from gov.uk's style guides found at:

- [https://github.com/alphagov/styleguides/blob/master/git.md](https://github.com/alphagov/styleguides/blob/master/git.md)

As mentioned in the previous section, context transfer is the main goal for writing easy to maintain software.  Writing good commit messages is one way to do this.  An example of a good commit message

```
Write better commit messages

The first line says what the commit does and should be kept under 50
characters, a blank line is inserted after it.  The full context of the
commit is expanded on in any text that comes after.  Use this space to
talk about the **why** of the code change and any consequences the
changes might have.

Depending on the group you are working in, you might be required to hard
wrap your longer content at 72 characters to make the messages more
readable when shown on the terminal with `git log`.

When making a new PR on GitHub for a branch that only has one commit the
first line of the commit will be used as the default title of the PR and
the longer message used as the PR's default text.  If you are hard
wrapping lines your PR's text will look odd in the browser's text input
box.

If you are fixing an issue reported on GitHub include the issue number
in the message as:

- close #XXX
- closes #XXX
- closed #XXX
- fix #XXX
- fixes #XXX
- fixed #XXX
- resolve #XXX
- resolves #XXX
- resolved #XXX

GitHub will automatically close the mentioned issue once the PR is
merged into the repo's **default** branch.
```

## Writing good PRs

These notes are partially adapted from gov.uk's style guides found at:

- [https://github.com/alphagov/styleguides/blob/master/pull-requests.md](https://github.com/alphagov/styleguides/blob/master/pull-requests.md)


## Making a good code review
Code review

## Good practices
Keeping a clean main branch
Tagging releases
Keeping branches up to date (e.g. rebase) and short lived
Writing good commit messages and PR messages

## CI/CD (quick touch on what these are and where they live inside a Git repository)
Setting up GitHub Actions to run tests and style checks

## How the Zooniverse manages GitHub repositories (as an example of a system that works well)
