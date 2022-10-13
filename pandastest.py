# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 13:10:47 2022

@author: kajun
"""

import pandas as pd
import numpy as np

frames = 2
data = np.zeros(frames)

k_df = pd.DataFrame(columns=["Frame:", "Pancake pixels", "Frazil pixels","Total pixels", "%pancake","%frazil","Sea-ice concentration:"])
#col =["Frame:", "Pancake pixels", "Frazil pixels","Total pixels", "%pancake","%frazil","Sea-ice concentration:"]
#data1 = {"Frame":1, "Pancake pixels":2, "Frazil pixels":3,"Total pixels"4, "%pancake":5,"%frazil":6,"Sea-ice concentration:":7
data2 = [8,9,10,11,12,13,14]
convert2 = pd.Series(data2,index=k_df.columns)
data3 = [1,2,3,4,5,6,7]
convert3 = pd.Series(data3,index=k_df.columns)
k_df = k_df.append(convert2,ignore_index=True)
k_df = k_df.append(convert3,ignore_index=True)
                   
                   
        #           , ignore_index=True)

