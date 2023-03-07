''' A python script that reduces that Zooniverse data from the extraction script. '''

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
    n_evals: int
             Number of unique users that have evaluated the task for the image
    img_df: DataFrame
            DataFrame for image
    '''

    df = pd.read_csv(fn)
    subject_id = df['subject_ids']
    ids = subject_id.unique()
    ids = sorted(ids)
    img_id = ids[img_num]
    img_df = df.loc[subject_id == img_id]
    n_evals = len(df['user_id'].unique())
    
    return img_id, n_evals, img_df


def run_all_tasks():

    for n in range(0,5):
        fn = "T" + str(n) + ".csv"
        df = pd.read_csv(fn)
        img_num = len(df['subject_ids'].unique())

        c = np.zeros(img_num)
        cr = np.zeros(img_num)
        a_inf = np.zeros(img_num)
        # loop over each image
        for i in range(0,img_num):
            img_id[i], n_evals[i], img_df = import_img_data(fn, i)
            if n == 0:
                output = task0(img_df)
            if n == 1:
                output = task1(img_df)
            if n == 2:
                output = task2(img_df)
            if n == 3:
                output = task3(img_df)
            if n == 4:
                output = task4(img_df)

            c[i], cr[i], a_inf[i] = output

            df = pd.DataFrame({'img_id': img_id, 'consensus': c, 'consensus_reached': cr, 'aux_info': a_inf}) 
            df.to_csv("consensus" + fn, index=False)


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
    consensus_reached = False  # contains wether or not a consensus has been reached
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

    return consensus, consensus_reached, None

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

    return center_list, consensus_flag, None

 
# task 3
def task3(img_df):
    #dostuff
    return consensus, consensus_reached, aux_info


# task 4
def task4(img_df):
    #dostuff
    return consensus, consensus_reached, aux_info

# unittests in a separate file / or here ?

