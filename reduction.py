''' A python script that reduces that Zooniverse data from the extraction script. '''

import pandas as pd
import numpy as np
import sklearn

# summary_image of image function that tells for a specific function what the evaluation provides

# summary_all_images()

# count_user_evaluations


# evaluate_task
def evaluate_tasks(img_df, specfic_task_evaluation, task_threshold):
    ''' A function frame for task evaluation, which checks if the threshold of task evaluations is passed. It further defines what the output of task evaluations must be.

    Parameters
    __________
    img_df : Dataframe
             Image Dataframe
    specific_task_evaluation: Python Function
             Function that evaluates specific
    task_threshold : int
             The number of minimum people that are required for this specific task to evaluate consensus 

    Returns
    _______
    consensus : Task specific
                Different tasks will return different consensus summary statistics
    consensus_flag : bool
                Flag that returns true or false depending on wether a consensus is reached or not

    aux_info : Task specific
                Additional information relating to the task
    '''

    consensus = None  # contains the information describing what the consensus is
    censensus_reached = False  # contains wether or not a consensus has been reached
    aux_info = None  # contains additinoal information, e.g. the significance of the consensus

    if count_user_evaluations(imgid) > task_threshold:

          consensus, consensus_reached, aux_info = specific_task_evaluation(img_df)

    return consensus, consensus_reached, aux_info

# task specific evaluation functions


# task 0
def task0(img_df):
    #dostuff
    return consensus, consensus_reached, aux_info


# task 1
def task1(img_df):)
    #dostuff
    return consensus, consensus_reached, aux_info

# clustering function

# compute_mean_and_std

# get_coordinates

# task 2    
def task2(img_df):
    ''' A function that evaluates task2 assumming that the minimum threshold of evaluations is met.

    Parameters
    __________
    img_df : Dataframe
             Image Dataframe
    Returns
    _______
    consensus : Task specific
                Different tasks will return different consensus summary statistics
    consensus_flag : bool
                Flag that returns true or false depending on wether a consensus is reached or not
  
    aux_info : Task specific
                Additional information relating to the task
    '''

    coordinates = get_coordinates(img_df)
    eps = 0.5
    min_samples = 5

    # read for imgid the x,y coordinates out
    # give them to the clustering function
    # return consensus ( i.e. mean positions and maybe their uncertainty), consensus_reached flag (True/False), auxilary info for the coding 
    
    clustering = sklearn.cluster.DBSCAN(eps, min_samples).fit(coordinates)
    
    center_list = np.zeros(shape = clustering.n_features_in_)
    
    for i in range(clustering.n_features_in_):
        
        center_list[i] = np.mean(coordinates[clustering.labels_==i], axis = 0)
    
    consensus_flag = 1
    if clustering.n_features_in_ == 0:
  	consensus_flag = 0

    return center_list, consensus_flag, clustering.labels_, clustering.n_features_in_

# task 3   
def task3(radius, clustering.labels_, clustering.n_features_in_):
   ''' A function that evaluates task3, using the task2 function to implement clustering labels.
   
   Parameters
   __________
   radius : Dataframe
   	    Radius Dataframe
   clustering.labels_ : List
   	                List of the central points (x,y) of each cluster found in task2
   clustering.n_features_in_ : Integer
                               The number of clusters found in task2
   Returns
   _______
   cluster_radius_list : List
                         List of the mean radius of each cluster
   consensus_flag : bool
                    Flag that returns true or false depending on wether a consensus is reached or not
   '''
                               

    # Reads the list of central points of the clusters.
    # Reads in all of the radii associated with each specific cluster and find the mean.
    # also checks consensus if no clusters found.
    
    cluster_radius_list = np.zeros(shape = clustering.n_features_in_)
    
    for i in range(clustering.n_features_in_):
    
    	cluster_radius_list[i] = np.mean(radius[clustering.labels_==i])
    	
    consensus_flag = 1
    if clustering.n_features_in_ == 0:
  	consensus_flag = 0
    	
    return cluster_radius_list, consensus_flag


# task 4
def task4(img_df):
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
