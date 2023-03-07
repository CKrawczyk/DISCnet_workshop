import pandas as pd
import numpy as np
import sklearn

# summary_image of image function that tells for a specific function what the evaluation provides

# summary_all_images()

# count_user_evaluations

def import_img_data(fn,img_num):
    '''Read CSV file and create DataFrame for specific image

    Parameters
    ----------
    fn : string
         CSV file name
    img_num: int
             Image number (at most the number of unique images in file)

    Returns
    -------
    img_id: int
            Image ID
    img_df: DataFrame
            DataFrame for image
    '''

    df = pd.read_csv(fn)
    subject_id = df['subject_id']
    ids = subject_id.unique()
    ids = sorted(ids)
    img_id = ids[img_num]
    img_df = df.loc[subject_id == img_id]
    
    return img_id, img_df

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
def task0(img_df):
    #dostuff
    return consensus, consensus_reached, aux_info


# task 1
def task1(img_df):
    '''Determine the consensus number of cats in an image

    Parameters
    ----------
    img_df: DataFrame 
            Image data

    Returns
    -------
    consensus: Int
               Consensus value of number of cats
    consensus_reached: Bool
                       True if consensus is selected by over 70% of voters
    '''

    img_df_clean = img_df.dropna()
    n_cats = img_df_clean['value']
    consensus = stats.mode(n_cats)
    max_pcnt = n_cats.count(consensus)/len(n_cats) * 100
    if max_pcnt < 70:
        consensus_reached = False
    else:
        consensus_reached = True

    return consensus, consensus_reached

# clustering function

# compute_mean_and_std


# task 2    
def task2(imgid, coordinates, eps, min_samples):

    # read for imgid the x,y coordinates out
    # give them to the clustering function
    # return consensus ( i.e. mean positions and maybe their uncertainty), consensus_reached flag (True/False), auxilary info for the coding 
    
    clustering = sklearn.cluster.DBSCAN(eps, min_samples).fit(coordinates)
    
    center_list = np.zeros(shape = clustering.n_features_in_)
    
    for i in range(clustering.n_features_in_):
        
        center_list[i] = np.mean(coordinates[clustering.labels_==i], axis = 0)
        
    return center_list

 
# task 3
def task3(img_df):
    #dostuff
    return consensus, consensus_reached, aux_info


# task 4
def task4(img_df):
    #dostuff
    return consensus, consensus_reached, aux_info

# unittests in a separate file / or here ?

