#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:38:57 2018

@author: BEI
"""
import os
import numpy as np
import nibabel as nb
from glob import glob

path = r'../data'

path_patient = glob(path + os.sep + '*')
path_patient = path_patient[:1]

data_orig = {}
data_pre = {}
label = {}

for i in path_patient:
    name_patient = i.split(os.sep)[-1]
    
    path_orig = glob(i + os.sep + 'orig' + os.sep + '*.nii.gz')
    for j in path_orig:
        name_orig = j.split(os.sep)[-1]
        name_orig = name_orig.split('.')[0]
        data_orig_init = nb.load(j)
        data_orig[name_patient + '_' + name_orig] = data_orig_init.get_data()
        
    path_pre = glob(i + os.sep + 'pre' + os.sep + '*.nii.gz')
    for j in path_pre:
        name_pre = j.split(os.sep)[-1]
        name_pre = name_pre.split('.')[0]
        data_pre_init = nb.load(j)
        data_pre[name_patient + '_' + name_pre] = data_pre_init.get_data()

    label_init = nb.load(i + os.sep + 'segm.nii.gz')
    label[name_patient] = label_init.get_data()






