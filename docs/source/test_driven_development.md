# Test driven development
When writing code you want to make sure the code works as intended, previously identified bugs stay fixed, and the code being written can solve the desired research question.  Test driven development is a way to systematically achieve these goals.

## What are tests
The basic function of a test is to pass a given input to your code that has **a known** output and check that the output matches your expectations.  The key here is the known output you are testing against comes from some source that is **not** your code (e.g. an analytic solution, work it out by hand, some other code you know works, etc...).

These test cases are written as functions within your code and can be run at any time to ensure any changes made in the code have not broken these test cases.  Using CI you can set up your code repository to run these tests any time a new PR is made and block the PR from merging if any of the tests fail.

When bugs arise in your code, it is best practice to first write a new test that reproduces the bug before fixing the bug.  That way you can be sure the bug is identified, fixed, and changes made in the future will not reintroduce the same bug into your code.

Once you become comfortable with writing tests you may find it easier to write your tests first and the code second.  Doing this encourages you to think about the main goals of the code you are about to write, and when the tests pass you know the code is finished.  This process of writing the test first is know as test driven development.

## Python's built in unittest library
Python comes with a built in testing library called [unittest](https://docs.python.org/3/library/unittest.html) that includes full object mocking capabilities.  Unittest organizes tests into classes (subclassed from `unittest.TestCase`) where each test is a method on the class that has a name starting with `test_`.  There are also special `setUp` and `tearDown` methods that, if defined, will run before and after *each* test method.  This class also provides various assert functions such as `self.assertEqual`, `self.assertDictEqual`, and `self.assertGreater` (see [API documentation for full list](https://docs.python.org/3/library/unittest.html)) that provide more useful error messages when they fail than a plain `assert` statement does.  All the examples in this workshop use `unittest`'s framework and syntax. 

Python will auto-discover any tests that are in your current directory by looking for any files that follow the pattern `test*.py` by default (this search pattern can be changed when the unittest command is run).  The test file must be importable from the top level directory of the project (i.e. a blank `__init__.py` is in the folders containing any tests).  Test can be run with the command:

```bash
python -m unittest discover
```

If this command does not find your tests you can specify various command line options to help it out, see [the discover documentation](https://docs.python.org/3/library/unittest.html#test-discovery) for more information.

## Other python testing libraries
The other commonly used python testing library is [pytest](https://docs.pytest.org/en/latest/).  It has its own syntax for writing tests that is more compact than `unittest`, but can come at the cost of clarity for more complex tests.  Pytest is also fully compatible with tests written in `unittest` syntax.

```{note}
VScode uses `pytest` to run tests inside the editor, if you are using `unittest`'s `self.subTest` syntax you will need to install the [pytest-subtests](https://github.com/pytest-dev/pytest-subtests) package for them to run as expected.
```

```{warning}
You might also see [nosetest](https://nose.readthedocs.io/en/latest/) used by some older packages, this testing framework is no longer in active development and should not be considered for new projects.
```

## Types of tests
There are several flavors of tests that can be written for code.  The main three I have come across are:
- Unit tests
- Integration tests
- Validation tests

While these are not the only three types of tests, they are a good starting point for writing your own tests.  

```{note}
These are the names that make the most sense to me, but others might use different names for the same kinds of tests.
```

### Unit tests 
The goal of unit tests are to test a "unit" of code (e.g. a single function definition or a single class method) in **isolation** from all the other units of code that make up the software.  These test are mostly for checking if the unit of code works as written (i.e. the algorithm was coded correctly).  Here is an example of a simple unit test:

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
The goal of integration tests are to test if multiple units of code work **together** correctly.  For example if you had a function who's only job is to call two other functions in a particular order and pass the results from one function into the next, an integration test would check exactly these things.  It would **not** check that the two sub-functions return the correct values (that is the job of a unit test for those sub-functions), just that that values passed back are sent to the correct place.

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
        # a traditional unit test to check an known input gives a known output
        expected = 6
        result = run_all(3)
        self.assertEqual(result, expected)

    @patch('package.file.func_2')
    @patch('package.file.func_1')
    def test_run_all_calls(self, mock_func_1, mock_func_2):
        '''Test run_all calls the inner functions with the expected values'''
        # an integration test to check data is being pass around as expected
        
        # we can input any value, the `result` will not change because of the mocks
        input_value = 3
        result = run_all(input_value)
        
        # test func_1 called with the argument provided to run_all
        mock_func_1.assert_called_once_with(input_value)

        # test func_2 called with the return value of func_1
        mock_func_2.assert_called_once_with(mock_func_1.return_value)

        # test run_all returns the func_2 return value
        self.assertEqual(result, mock_func_2.return_value)
```

```{warning}
When writing integration tests (or any tests using mocks) it is very easy to make a test that is too strongly coupled with the code.  Any adjustments to the source code would **require** the test to be adjusted as well.  The unit test in this example is not strongly coupled, the integration test is.

To help avoid this, when you have finished writing a test read it over and ask yourself "what is the main goal of the code being tests and do these test check **only** that?  Is a future refactor likely to break this test?"

If the main goal `run_all` is to get the expected result out the other end, the unit test is sufficient.  If the main goal of `run_all` is to compose `func_1` and `func_2` the integration test is sufficient.
```

### Validation tests
The goal of validation tests are to check if the code written is appropriate for problem you are trying to solve (i.e. is the code using the correct algorithm).  For example, can you get away with using a 2nd order ODE integrator or do you need to using a 4th order one to keep the desired level of accuracy.  Often these are just a flavor of an integration test or unit test, but with "science quality" data being passed in.

## Test coverage
Test coverage is a way of tracking what lines of your source code were run when each of your tests ran.  When writing tests for a function you goal should be to have as much coverage as possible.  This typically means making sure you have at least one test for every branch in your code (i.e. one test for each `if` branch in the code).  Sometimes when writing your tests you will realize that there are branches in your code that can never be reached and can be safely removed from the code.

To check test coverage you can use the [coverage package](https://coverage.readthedocs.io/en/latest/), once installed it will wrap around your chosen test runner and check how many lines of you package's code were run by your tests.  After the tests are run you can generate a report to see how many lines were covered.  The basic usage is:

```bash
coverage run --source data_transforms --omit *test* -m unittest discover
coverage report --show-missing
```

The options passed to `run` are:
- `--source data_transforms`: base folder for the package
- `--omit *test*`: pattern of files not to include in coverage percent
- `-m unittest discover`: the test runner command

The option passed to `report` is:
- `--show-missing`: for each file list the line number(s) not covered by any tests

These extra command line options can be included in your project's `pyproject.toml` file (already done in this workshop's repo) to simplify these commands to:

```bash
coverage run
coverage report
```

This leaves you with an easy to remember command for running your tests with all the project specific options placed in a single configuration file.

## Mocks
In the integration tests section above the example makes use of what are called "function mocks."  These are special classes that are used to **fully replace** another function or class.  This mock will keep track of how many times it is called, what arguments and keywords it was called with, and what it should return when called.  

The easiest way to use a mock is with the `@patch` decorator, this takes the full import path of the object to be mocked, and an optional `return_value` specifying what value should be returned when the mock is called.  By default any method or return value accessed on a mock is also a mock, so there is no need to know the full object spec beforehand.

```{note}
The import path should be an absolute path to the object being mocked starting at the top level of your package.
```

The main use of mocks are:
- testing pipeline code passes data around correctly
- replace functions that take a long time to run with an object that returns instantly
- ensuring that bugs in sub-functions don't make other functions' tests fail (i.e. only testing the code you wrote and not the code coming from other packages). 
- avoid having to read/write data to disk (`unittest.mock.mock_open` is its own function that helps when you need to test code that opens files)

Example, we want to mock away a class that has several methods (we will use a `with` block this time instead of the decorator syntax):

```python
from unittest.mock import patch, call

# make an instance of a class we will mock
thing = object()

# Set what the mocked `method_1` and `method_2` should return
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
    assert thing.method_2(a=5) == 1
    assert thing.method_2(a=6) == 2
    assert thing.method_2(a=7) == 3

    # how to test it was called three times with specific arguments/keywords each time
    expected_calls = [
        call(a=5),
        call(a=6),
        call(a=7)
    ]
    mock_MyClass.method_2.assert_has_calls(expected_calls, any_order=False)

    # how to test it was called three times (without specifying the explicit calls)
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

See [https://docs.python.org/3/library/unittest.mock.html](https://docs.python.org/3/library/unittest.mock.html) for more examples of mocks and their uses.
