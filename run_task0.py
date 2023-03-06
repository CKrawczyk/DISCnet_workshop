import pandas as pd
import numpy as np
import statistics as stats

arr = pd.read_csv()

def task1(action):
    num_arr = action
    length = len(num_arr)
    ones = num_arr.count(1)
    twos = num_arr.count(2)
    threes = num_arr.count(3)
    total = ones+twos+threes
    mode = stats.mode(num_arr)
    mode_num = num_arr.count(mode)
    pcnt_ones = np.round((ones/total) * 100)
    pcnt_twos = np.round((twos/total) * 100)
    pcnt_threes = np.round((threes/total) * 100)
    list = [pcnt_ones, pcnt_twos, pcnt_threes]
    max_pcnt = max(list)
    if max_pcnt < 70:
        flag = 'No Consensus'
    else:
        flag = "Consensus"
    return mode, pcnt_ones, pcnt_twos, pcnt_threes, max_pcnt, flag, length

xx = task1(arr)
print(xx)