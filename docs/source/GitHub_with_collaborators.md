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

## Git workflow

There are many different ways to effectively use git within a collaboration, and many more ways to have it be a nightmare.  For this workshop we will use the workflow I am most familiar with and encourages writing maintainable code.  The workflow is as follows:

1. checkout the latest `main` branch
```bash
git checkout main
git pull
```
2. make a new branch with a descriptive name
    - for better organization of branch names you can prepend branch names with `feature/`, `bug/`, `hotfix/`
```bash
git checkout -b my-feature-branch
```
3. write your code and group logical units of changes into individual commits
```bash
git add my_new_file.py
git commit
```
4. push the changes to a common remote repository and open a PR on GitHub
```bash
git push --set-upstream origin my-feature-branch
```
5. assign a reviewer for your PR (it is your job to ask someone to look at your code, don't expect the PR to "just be seen" by other developers)
6. address any feedback left by the reviewer
7. once approved **rebase** your changes onto the latest `main` branch to ensure there are no code conflicts
```bash
git checkout main
git pull
git checkout my-feature-branch
git rebase main
```
or if you want to clean up your git history (e.g. merge two commit together, change your commit messages, etc...)
```bash
git rebase -i main
```
8. push the rebased code back to the remote
```bash
git push --force-with-lease origin my-feature-branch
```
9. merge to the `main` branch using the big green button
10. delete the brach on the remote once the merge is finish
11. pull the latest `main` (with your PR merged) locally
```bash
git check main
git pull
```
12. (optional) delete your local copy of the merged branch
```bash
git branch -d my-feature-branch
```

What does this workflow achieve?
- It ensures only reviewed code makes it into the `main` branch
    - This implies the `main` branch is where you will always be able to find a working version of the code
- It encourages short lived feature branches
    - Smaller code changes are easier to review and less likely to conflict with other developers' code changes
- As the code writer you are responsible for addressing merge conflicts
- By using `rebase` rather than `merge` the git history is kept linear
- Once given the OK by the reviewer the code writer makes the final decision on when to merge
- Any merged branch can be safely deleted, there is no need to clutter up the remote with old branches (also you are less likely to have multiple developers pick the branch name for their work if there are fewer branches on the remote repo).
