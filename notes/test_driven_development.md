# Test driven development

## Overview: What problems do tests solve?

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

<add example of unit test>

### Integration tests
The goal of integration tests are to test if multiple units of code work **together** correctly.  For example if you had a function who's only job is to call three other functions in a particular order and pass the results from one function into the next, an integration test would check exactly these things.  It would **not** check that the three sub-functions return that correct values (that is the job of a unit test), just that that values passed back are sent to the correct place.

<add example of integration test>

### Validation tests
The goal of validation tests are to check if the code written is appropriate for problem you are trying to solve (i.e. is the code using the correct algorithm).  For example, can you get away with using a 2nd order ODE integrator or do you need to using a 4th order one to keep the desired level of accuracy.  Often these are just a flavor of an integration test, but with "science quality" data being passed in.

<add example of validation tests>

## Test coverage
Test coverage is a way of tracking what lines of your code were run when each of your tests ran.  When writing tests for a function you goal should be to have as much coverage as possible.  This typically means making sure you have at least one test for every branch in your code (i.e. one test for each `if` branch in the code).  Sometimes when writing you tests you will realize that there are branches in your code that can never be reached and can be safely removed from the code.

## Common pitfalls (e.g. don’t over test)
The most common pitfall I run into when writing tests is "over testing".  This means that I have written a test that is to strongly coupled with the code, and any adjustment to the code would break the test, even if the output is identical.  This typically happens with integration tests or when mocking away function calls (see below).  To help avoid this, when you have finished writing a test read it over and as yourself "what is the main goal of the code being tests and does this test only that?"

<add example of over tested code>

## Mocks (quick touch on what they are and when they are useful)

<add example of mock>

## Overview of python testing frameworks 

## Tox setup (quick touch on what this is, related to CI above)
