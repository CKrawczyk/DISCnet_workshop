# The task
In this workshop we will all be helping to write a single python package.  This package will be used to process the results of a [test Zooniverse project](https://www.zooniverse.org/projects/cmk24/testing/classify).  In this Zooniverse project volunteers are asked to answer some questions, count, and draw features on stock images of cats.

## The data
The data comes as a [Zooniverse classification export](https://help.zooniverse.org/next-steps/data-exports/#classification-export), a CSV file containing one row for every classification made on the project.  An example of this data file can be found in the [example_data](https://github.com/CKrawczyk/DISCnet_workshop/tree/main/example_data) folder of the repository.  The link above contains an explanation of what data is contained within the file, we will mostly be working with the `annotations` column for this workshop.

The project's workflow has:
- A question task (task label `T0`)
- A text task (task label `T1`)
- A point drawing task (task label `T2`)
- A circle drawing task (task label `T3`)
- A rectangle drawing task (task label `T4`)

The example data provided is enough for understanding the data format and writing the code specifications.  To generate the full data set we will all spend some time classifying on this project and generate a more complete data export on the second day of the workshop.

## The data analysis plan
For this data analysis we want to do two things:

1. **Extract** the relevant data for each task into a **flat** CSV file (one file per task)
2. **Reduce** all extracts from the same subject to find a consensus answer for each task

```{note}
This workshop is more focused on "how to write code" rather than the results of the data analysis.  Don't worry about getting the analysis "correct" or even finishing both tasks above, instead focus on the process of writing code as a team.
```

## The code structure
We will use this space to plan out our code structure.
