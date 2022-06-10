# The Task

In this workshop we will all be helping to write a single python package.  This package will be used to process the results of a [test Zooniverse project](https://www.zooniverse.org/projects/cmk24/testing/classify).  In this Zooniverse project volunteers are asked to draw some shapes, describe, or label features on stock cat images.

## The data

The data comes in the from of a [Zooniverse classification](https://help.zooniverse.org/next-steps/data-exports/#classification-export) CSV file.  An example of the data can be found in the `example_data` folder of the repository.  Each row of the data contains one classification with the `annotations` column containing the answers the volunteer gave for each task they worked through.

The project's workflow has:
- A question task
- A text task
- A point drawing task
- A circle drawing task
- A rectangle drawing task

To generate the full data set we will all spend some time classifying on this project and generate a data export in the afternoon.

### The data analysis plan

For the data analysis we want to do two things:

1. **Extract** the relevant data for each task into a **flat** CSV file (one file per task type)
2. **Reduce** all extracts from the same subject to find a consensus answer for each task

#### The code structure

We will use this space to plan out our code structure.
