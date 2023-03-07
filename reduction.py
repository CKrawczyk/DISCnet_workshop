import pandas as pd
import numpy as np
import sklearn

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


# Clustering and finding central points of each cluster
def clustering(coordinates, eps, min_samples):

    # read for imgid the x,y coordinates out
    # give them to the clustering function
    # return consensus ( i.e. mean positions and maybe their uncertainty), consensus_reached flag (True/False), auxilary info for the coding 
    
    clustering = sklearn.cluster.DBSCAN(eps, min_samples).fit(coordinates)
    
    center_list = np.zeros(shape = clustering.n_features_in_)
    
    for i in range(clustering.n_features_in_):
        
        center_list[i] = np.mean(coordinates[clustering.labels_==i], axis = 0)
        
    return center_list, clustering.labels_, clustering.n_features_in_
    
    
def task3_radius(radius, center_list, clustering.labels_, clustering.n_features_in_):

    # Reads the list of central points of the clusters.
    # Reads in all of the radii associated with each specific cluster and find the mean.
    
    cluster_radius_list = np.zeros(shape = clustering.n_features_in_)
    
    for i in range(clustering.n_features_in_):
    
    	cluster_radius_list[i] = np.mean(radius[clustering.labels_==i])
    	
    return cluster_radius_list
    	

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