#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:59:38 2017

@author: rob
"""

# Importing libraries
import numpy as np
import pandas as pd
from gender_detector.gender_detector import GenderDetector

# Importing data    
dataset = pd.read_json("https://data.cityofnewyork.us/resource/4qxi-jgbe.json?$$app_token=2k2aLRGeC9aJ4prhwgaQv0Rar")

# Processing data
detector = GenderDetector('us')
new = dataset.assign(gender = lambda x: detector.guess(x['first_name']))