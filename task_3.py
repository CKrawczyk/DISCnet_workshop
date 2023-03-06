import pandas as pd
import numpy as np
import json

def discnet_t3(shared_df):
    # Create empty array
    df_t3 = np.zeros((len(shared_df),3))
    # Add r, x, y to array, ignore empty lines
    for i in range(len(shared_df)):
        try:
            df_t3[i,0] = shared_df.iloc[i][3]['value'][0]['r']
            df_t3[i,1] = shared_df.iloc[i][3]['value'][0]['x']
            df_t3[i,2] = shared_df.iloc[i][3]['value'][0]['y']
        except:
            pass
    # Mark empty lines as Nan
    df_t3[df_t3 == 0] = np.nan
    # Transfer into Pd dataframe
    d_pre = {'r': df_t3[:,0], 'x': df_t3[:,1],'y': df_t3[:,2]}
    df_t3_pre = pd.DataFrame(data=d_pre)
    return df_t3_pre