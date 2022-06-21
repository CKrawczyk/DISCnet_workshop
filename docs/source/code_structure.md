# Code and file structure

One of the key things to keep in mind when writing code in a team is that other people will be reading and reviewing you code.  To that end it is always worth the time make the process of reading your code as easy as possible.

## Organizing your code

Step one in making your code more readable is to organize it into different files and folders.  Some rules that help with this:

- Every file has one large function, one class, or collection of related small functions
    - The file name should reflect what the code in the file does
- Group the files by the general task they complete (e.g. a folder of plotting code and a folder for analysis)
    - The folder name should reflect this general task

It is OK if you don't have a full plan for what these file and folder structures will look like before you start, you can always re-organize your code after it is written.  The important thing is to have it be at least somewhat organized before code review.  Any question you have about this structure you can alway flag up for your reviewer to take a look at and help answer.

## Code legibility

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
