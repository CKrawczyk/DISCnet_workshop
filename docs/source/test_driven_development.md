# Test driven development


## Overview: What problems do tests solve?
When writing code you want to make sure the code works as intended, when bugs are found that then don't come back, and the code being written can solve the research question being asked of it.  Test driven development is a way to systematically achieve all of these goals.


## What are tests
The basic function of a test is to take in a given input to your code that has **a known** output, run your code on the input, and check that the output matches your expectations.  The key here is the known output you are testing against comes from some source that is **not** your code (e.g. an analytic solution, work it out by hand, some other code you know works, etc...).

These test cases are written as functions within your code and can be run at any time to ensure any changes made in the code have not broken any of the tests.  Using CI (e.g. GitHub actions) you can set up your code repository to run your tests any time a new PR is made and block the PR from merging if any of the tests fail.

When bugs arise in your code, it is best practice to first write a new test that reproduces the bug before fixing the bug.  That way you can be sure changes made in the future will not reintroduce the bug that was fixed.

Once you become comfortable with writing tests you may find it easier to write your tests first and the code second.  Doing this forces you to think about the main goals of the code you are about to write are, and gives a clear stopping point as you know once you have reached these goals (i.e. when the tests pass you can stop writing code).


## Types of tests
There are several flavors of tests that can be written for code.  The main there that I have come across are:
- Unit tests
- Integration tests
- Validation tests

While these are not the only three types of tests, they are a good starting point for writing your own tests.  Note: these are the names that make the most sense to me, but others might use different names.


### Unit tests 
The goal of unit tests are to test a "unit" of code (e.g. a single function definition) in **isolation** from all the other units of code that make up the software.  These test are mostly for checking if the unit of code works as written (i.e. the algorithm was coded correctly).

```python
def func(a, N=1):
    return a + N
```

```python
import unittest
from package.file import func


class TestFunc(unittest.TestCase):
    def test_func_default_N(self):
        '''Test func with default N value'''
        expected = 3
        result = func(2)
        self.assertEqual(result, expected)
    
    def test_func_with_N(self):
        '''Test func with N keyword set'''
        expected = 4
        result = func(2, N=2)
        self.assertEqual(result, expected)
```

### Integration tests
The goal of integration tests are to test if multiple units of code work **together** correctly.  For example if you had a function who's only job is to call three other functions in a particular order and pass the results from one function into the next, an integration test would check exactly these things.  It would **not** check that the three sub-functions return that correct values (that is the job of a unit test), just that that values passed back are sent to the correct place.

```python
def func_1(a):
    return a + 1


def func_2(b):
    return b + 2


def run_all(a):
    b = func_1(a)
    c = func_2(b)
    return c
```

```python
import unittest
from unittest.mock import patch
from package.file import run_all


class TestRunAll(unittest.TestCase):
    def test_run_all_value(self):
        '''Test run_all give expected value'''
        # a traditional unittest to check an known input gives a known output
        expected = 6
        result = run_all(3)
        self.assertEqual(result, expected)

    @patch('package.file.func_2', return_value=6)
    @patch('package.file.func_1', return_value=4)
    def test_run_all_calls(self, mock_func_1, mock_func_2):
        '''Test run_all calls the inner functions with the expected values'''
        # an integration test to check data is being pass around in the the
        # expected way inside the function
        result = run_all(3)  # input will not change output because mocks are used
        
        # test func_1 called with the argument provided to run_all
        mock_func_1.assert_called_once_with(3)
        # test func_2 called with the return value of func_1
        mock_func_2.assert_called_once_with(4)
        # test run_all returns the func_2 return value
        self.assertEqual(result, mock_func_2.return_value)
```


### Validation tests
The goal of validation tests are to check if the code written is appropriate for problem you are trying to solve (i.e. is the code using the correct algorithm).  For example, can you get away with using a 2nd order ODE integrator or do you need to using a 4th order one to keep the desired level of accuracy.  Often these are just a flavor of an integration test, but with "science quality" data being passed in.


## Test coverage
Test coverage is a way of tracking what lines of your code were run when each of your tests ran.  When writing tests for a function you goal should be to have as much coverage as possible.  This typically means making sure you have at least one test for every branch in your code (i.e. one test for each `if` branch in the code).  Sometimes when writing you tests you will realize that there are branches in your code that can never be reached and can be safely removed from the code.


## Mocks
In the integration tests section above the example makes use of what are called "function mocks."  These are special classes that are used to **fully replace** an function or class.  This mock will keep track of how many times it is called, what arguments and keywords it was called with, and what what it should return when called.  

The easiest way to use a mock is with the `@patch` decorator, this takes the full import path of the object to be mocked, and an optional `return_value` specifying what value should be returned when the mock is called.  By default any method or return value accessed on a mock is also a mock, so there is no need to know the full mock spec beforehand.

The main use of mocks are:
- testing pipeline code passes data around correctly
- replace functions that take a long time to run with an object that returns instantly
- ensuring that bugs in sub-functions don't make other functions' tests fail (i.e. only testing the code you wrote and not the code coming from other packages). 
- avoid having to read/write data to disk (`unittest.mock.mock_open` is its own function that helps when you need to test code that opens files)

Example, we want to mock away class with some methods (we will use a `with` block this time instead of the decorator):

```python
from unittest.mock import patch, call


thing = object()
config = {
    'method_1.return_value': 5,
    'method_2.side_effect': [1, 2, 3]
}


with patch('__main__.thing', **config) as mock_MyClass:
    # check the mock applied
    assert thing is mock_MyClass

    # check method_1 returns what we set
    assert thing.method_1() == 5

    # how to test it is called exactly once
    mock_MyClass.method_1.assert_called_once()

    # check method_2 returns each values set in turn
    assert thing.method_2(a=1) == 1
    assert thing.method_2(a=2) == 2
    assert thing.method_2(a=3) == 3

    # how to test it was called three times with specific arguments/keywords each time
    expected_calls = [
        call(a=1),
        call(a=2),
        call(a=3)
    ]
    mock_MyClass.method_2.assert_has_calls(expected_calls, any_order=False)

    # how to test it was called three times with any arguments/keywords
    # Note: this would use self.assertEqual if inside a TestCase class
    assert mock_MyClass.method_2.call_count == 3

    # any method and return value generates a new mock that tracks calls
    thing.method_3().sub_method(a=1, b=2)

    # test this sub_method was called once with specific keywords
    mock_MyClass.method_3.return_value.sub_method.assert_called_once_with(a=1, b=2)

    # define new return_values on the mock object directly rather than passing them
    # into **config
    mock_MyClass.method_4.return_value = 'new value'

    assert thing.method_4() == 'new value'

# check the mock is no longer applied outside the with block
assert thing is not mock_MyClass
```

See https://docs.python.org/3/library/unittest.mock.html for more examples of mocks and their uses.


## Common pitfalls
The most common pitfall I run into when writing tests is "over testing" when using mocks.  This means that I have written a test that is to strongly coupled with the code, and any adjustment to the code would break the test, even if the output is identical.  

Take another look at the integration test example above.  In a future refactor of the code the calls to `func_1` and `func_2` might be replaced by one new function called `func_3` that returns equivalent values in all cases.  The first test `test_run_all_value` will still pass, but the second test `test_run_all_calls` will have to be rewritten to account for the refactor.

To help avoid this, when you have finished writing a test read it over and as yourself "what is the main goal of the code being tests and does this test only that?  Is a future refactor likely to break this test?"  Most of the time you don't really care how many times a function was called, just that it was called.


## Overview of python testing frameworks

### Python built in unittest library

Python comes with a built in testing library called [unittest](https://docs.python.org/3/library/unittest.html) that includes full object mocking capabilities.  Unittest organizes tests into classes (subclassed from `unittest.TestCase`) where each test is a method on the class that has a name starting with `test_`.  There are also special `setUp` and `tearDown` methods that, if defined, will turn before and after *each* test method.  This class also provides various assert functions such as `self.assertEqual`, `self.assertDictEqual`, and `self.assertGreater` (see [API documentation for full list](https://docs.python.org/3/library/unittest.html)) that provide more useful error messages when they fail than a plain `assert` statement does.  All the examples in this workshop use `unittest`'s framework and syntax. 

Python will auto-discover any tests that are in your current directory by looking for any files that follow the pattern `test*.py` by default (this search pattern can be changed when the unittest command is run).  The test file must be importable from the top level directory of the project (i.e. `__init__.py` in the folders containing any tests).  To run the tests use the command:

```bash
python -m unittest discover
```

If this command does not find your tests you can specify various command line options to help it out, see [the discover documentation](https://docs.python.org/3/library/unittest.html#test-discovery) for more information.

### test coverage

To check test coverage you can use the [coverage package](https://coverage.readthedocs.io/en/latest/), once installed it will wrap around your chosen test runner and check how many lines of you package's code were run by your tests.  After the tests are run you can generate a report to see how many lines were covered.  The basic usage is:

```bash
coverage run --source data_transforms --omit *test* -m unittest discover
coverage report --show-missing
```

The options passed to `run` are:
- `-source data_transforms`: base folder for the package
- `--omit *test*`: patter of files not to include in coverage percent
- `-m unittest discover`: the test runner command

The option passed to `report` is:
- `--show-missing`: for each file list the line number(s) not covered by a test

These extra command line options can be included in your project's `setup.cfg` file (already done in this workshop's repo) to simplify these commands to:

```bash
coverage run
coverage report
```

This leaves you with an easy to remember command for running your tests with all the project specific options placed in a single configuration file.

### Other testing libraries

The other commonly used python testing libraries are [pytest](https://docs.pytest.org/en/latest/) and [nosetest](https://nose.readthedocs.io/en/latest/) (note: `nosetest` is no longer being actively developed and should not be considered for new projects).  The each have a different syntax for writing test, but both of their test runners are able to find and run any tests written with the built in `unittest` syntax and are compatible with the `coverage` package.

As `unittest` is the most universal of these libraries we will be using it for this workshop.
