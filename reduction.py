import pandas as pd
import numpy as np

# summary_image of image function that tells for a specific function what the evaluation provides

# summary_all_images()

# count_user_evaluations


# evaluate_task
def evaluate_tasks(imgid, specfic_task_evaluation, task_threshold):

    consensus = None  # contains the information describing what the consensus is
    censensus_reached = False  # contains wether or not a consensus has been reached
    aux_info = None  # contains additinoal information, e.g. the significance of the consensus

    if count_user_evaluations(imgid) > task_threshold:

    consensus, consensus_reached, aux_info = specific_task_evaluation(imgid)

    return consensus, consensus_reached, aux_info

# task specific evaluation functions


# task 0
def task0(imgid):
    #dostuff
    return consensus, consensus_reached, aux_info


# task 1
def task1(imgid):)
    #dostuff
    return consensus, consensus_reached, aux_info

# clustering function

# compute_mean_and_std


# task 2
def task2(imgid):
    # read for imgid the x,y coordinates out
    # give them to the clustering function
    # return consensus ( i.e. mean positions and maybe their uncertainty), consensus_reached flag (True/False), auxilary info for the coding 
    return consensus, conensus_reached, aux_info

 
# task 3
def task3(imgid):
    #dostuff
    return consensus, consensus_reached, aux_info


# task 4
def task4(imgid):
    #dostuff
    return consensus, consensus_reached, aux_info

# unittests in a separate file / or here ?


# function to separate the DataFrame into DataFrames for each image
def separate_img(df):
    subject_id = df['subject_id']
    ids = subject_id.unique()
    ids = sorted(ids)

    img_df = []
    for i,ID in enumerate(ids):
        img_df.append(df.loc[subject_id == ID])

    return img_df
