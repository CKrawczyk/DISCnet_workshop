# Using GitHub with collaborators 

## Overview: What problem is Git and GitHub designed to solve?

At some point in your research you will likely have a massive hard drive crash, or realize you introduced a bug in your code and want to revert it back to its working state (perhaps from several weeks before). Or you may end up working on a bit of code with other people. In any of these cases version control saves the day.

In this workshop we will be using Git as our version control software, and GitHub as our remote repository service for working with collaborators.

## Basic concepts

While many of you might already be familiar with Git, let's make sure we are all on the same page and introduce some of the basic concepts:

- Repository: the name given to a folder that has Git version control set up
```bash
git init
```
- Local repository: The copy of a Git repository that is on your development computer
- Remote repository: The copy of a Git repository that is on the internet
- Pull from remote: The process of "pulling" the changes on the remote to you local
```bash
git pull
```
- Push to remote: The process of "pushing" local change to the remote
```bash
git push
```
- Staging changes: The process of adding files to be in the next commit
```bash
git add <file name>
```
- Commit: The process of creating a checkpoint you can return back to
```bash
git commit
```
- Branch: The process of creating a working space that allows changes to be made without effecting other branches
```bash
# make a new branch
git checkout -b <new branch name>
# move to an existing branch
git checkout <branch name>
# list all (local) branches
git branch
```
- Merge: The process of merging two branches together
```bash
git checkout main
git merge <branch name>
```
- Tag: The process of tagging a commit to make it easier to find in the future
```bash
git tag <tag name>
```

To make things easier you should configure Git:

```bash
git config --global user.name "<your name>"
git config --global user.email <your email>
git config --global core.editor <your text editor (defaults to vim)>
```

```{note}
If you want to use vscode as the default editor you can do that with: `git config --global core.editor "code -n --wait"`
```

Full Git documentation can be found in [The Git Book](https://git-scm.com/book/en), this include a good section about the motivation behind Git and the problems it was designed to solve.

### GitHub vs GitLab vs Bitbucket

While we are using GitHub for this workshop, it is not the only option for hosting remote git repositories.  The other major options are [GitLab](https://about.gitlab.com/) and [Bitbucket](https://bitbucket.org/product/).  For the most part all there platforms offer the same services but they sometimes use different terms.  Below is a table for converting between the terms used by each platform:

| GitHub         | GitLab        | Bitbucket           |
| :------------- | :------------ | :------------------ |
| Pull Request   | Merge Request | Pull Request        |
| Gist           | Snippet       | Snippet             |
| Repository     | Project       | Repository          |
| Organizations  | Groups        | Teams               |
| GitHub Actions | GitLab CI     | Bitbucket Pipelines |

## Git workflow

There are many different ways to effectively use git within a collaboration, and many more ways to have it be a nightmare.  For this workshop we will use the workflow I am most familiar with and encourages writing maintainable code.  The workflow is as follows:

1. checkout the latest `main` branch
2. make a new branch with a descriptive name
    - for better organization of branch names you can prepend branch names with `feature/`, `bug/`, `hotfix/`
3. write your code grouping logical units of changes into individual commits
4. push the changes to the common remote repository and open a PR on GitHub
5. assign a reviewer for your PR (it is your job to ask someone to look at your code, don't expect the PR to "just be seen" by other developers)
6. address any feedback left by the reviewer
7. once approved **rebase** your changes onto the latest `main` branch to ensure there are no code conflicts
or if you want to clean up your git history (e.g. merge two commit together, change your commit messages, etc...) rebase in interactive mode (`git rebase -i main`)
8. push the rebased code back to the remote
9. merge to the `main` branch using the big green button
10. delete the brach on the remote once the merge is finish
11. pull the latest `main` (with your PR merged) locally
12. (optional) delete your local copy of the merged branch

```bash
# get latest code on main branch
git checkout main
git pull

# make new working branch
git checkout -b my-feature-branch
git add my_new_file.py
git commit
git push --set-upstream origin my-feature-branch
# make PR on GitHub

# get latest changes to main and rebase
git checkout main
git pull
git checkout my-feature-branch
git rebase main
git push --force-with-lease origin my-feature-branch

# after merge on GitHub update your main branch
git checkout main
git pull

# clean up
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
- Any merged branch can be safely deleted, there is no need to clutter up the remote with old branches (also you are less likely to have multiple developers pick the same branch name for their work if there are fewer branches on the remote repo).

## Writing better commit messages

These notes are partially adapted from gov.uk's style guides found at:

- [https://github.com/alphagov/styleguides/blob/master/git.md](https://github.com/alphagov/styleguides/blob/master/git.md)

As mentioned in the previous section, context transfer is the main goal for writing easy to maintain software.  Writing good commit messages is one way to do this.  Here is an example of a good commit message:

```
Write better commit messages

The first line says what the commit does and should be kept under 50
characters, a blank line is inserted after it.  The full context of the
commit is expanded on in any text that comes after.  Use this space to
talk about the **why** of the code change and any consequences the
changes might have.

Depending on the group you are working in, you might be required to hard
wrap your longer context at 72 characters to make the messages more
readable when shown on the terminal with the `git log` command.

When making a new PR on GitHub for a branch that only has one commit the
first line of the commit will be used as the default title of the PR and
the longer message used as the PR's default text.  If you are hard
wrapping lines your PR's text will look odd in the browser's text input
box.  You may need to reformat it before opening the PR.

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

## Writing better PRs

These notes are partially adapted from gov.uk's style guides found at:

- [https://github.com/alphagov/styleguides/blob/master/pull-requests.md](https://github.com/alphagov/styleguides/blob/master/pull-requests.md)

Once you have a branch with some commits you want to merge into the main branch, the next step is to have those changes reviewed by another developer.  On GitHub this process is known as creating a Pull Request (PR).  When opening as PR you should provide a detailed description of changes introduced, the reason the changes were made, and any specific things they reviewer should be aware of when testing your code.  If the PR is in references to an open issue on the repo this should be mentioned as well.

## Writing better code reviews

When working in a team it is important to review other people's code along side writing your own code.  While it might be tempting to just quickly look code changes on GitHub and leave a short message like "looks good to me" that is only really useful for very small changes to the code.  For larger changes a full review should be done.

1. Pull down the changes locally
```bash
git checkout main
git pull  # also fetches the names of all remote branches
git checkout <name of branch on remote>
```
2. Read the PR to see what changes were made
3. Test that those changes work as intended
    - Do the unittest pass locally
    - Use the code that was changed, if you don't know how ask for an example use case on the PR
4. If the PR is fixing a bug:
    - Reproduce the bug on `main`
    - Switch to the PRs branch and ensure the bug is fixed
5. Look over the code diff on GitHub and leave inline comments you have about any of the lines
    - Questions about how code works
    - Suggestions for make the code easier to read and/or more efficient
6. Write your review (GitHub supports full markdown, don't be afraid to use section headings and lists in your review)
    - Open with a summary of the changes made, this allows the person who opened the PR to see if you understood the changes correctly
    - List the steps you took to test the code
    - Record any observations you made during the testing process
    - If appropriate list any consequences of the changes (e.g. is there other code that should be changed in a future PR as a result)
    - Any actions the PRs author(s) should take before merging
7. Either approve or block (pending changes) the PR
8. If approved you are done, it is the responsibility of the author(s) to merge the PR.  If not re-review when the changes asked for are finished.

Here is an example of well constructed PR and review taken from on of the Zooniverse's repositories [https://github.com/zooniverse/front-end-monorepo/pull/2313](https://github.com/zooniverse/front-end-monorepo/pull/2313).

## CI (continuous integration)

If you want to test your code automatically every time new code is committed you can set up CI.  These days this is easy to do on GitHub with GitHub Actions (GHA).  These are script you can write and place in the `.github/workflows` folder of the repository that contain instructions for creating a VM with you code in it.  Typically these actions are used to do things like:

- run all tests when new code is pushed to any branch
- run all tests against several version of python
- ensure test coverage does not fall below a given amount when new code is pushed
- check new code follows you chosen style

This repository has several GHA set up that fall under CI:

- Check coding style with `flake8` on any PR
- Run unit test and report coverage on any PR
- Check if any dependencies in `main` have new versions and open a PR that updates them if they do

GitHub can also be configured with branch protection that will ensure that particular GHAs must complete successfully before any code can be merged into it.

### tox

While GHA are great they only run tests in the cloud, so the turn around time can be slow when you want to test a change locally across different python versions.  [Tox](https://tox.wiki/en/latest/) is a way to automatically setup and run your tests across different python environments all on your local computer.  Tox can also be run directly in a GHA if you already have it set up for a project.

## CD (continuous delivery/deployment)

A related concept to CI is CD.  This takes the concept of CI and goes one step further by automatically taking changes to the `main` (or any other branch) and hosting them for use automatically.  These are also handled with GHA.  Typical examples are:

- re-deploying a website on a merge to `main`
- publish your code to [PyPi](https://pypi.org/) when the version number is bumped

This repository has one GHA set up that falls under CD:

- Build and host the package documentation on a merge to `main`
