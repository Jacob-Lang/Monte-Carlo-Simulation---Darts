# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:57:18 2019

@author: Jacob

Helper functions for the darts analysis
"""
import numpy as np
from math import atan2
import random


def throw(target, sigma):
    """Returns a dart position after a non-perfect throw"""
    
    x = random.gauss(target[0], sigma)
    y = random.gauss(target[1], sigma)

    dart_pos = np.array([x, y])
    
    return dart_pos

def score(dart_pos):
    """takes numpy array dart_pos = (x,y) and returns points scored at that position"""
    
    # polar coordinates
    r = np.linalg.norm(dart_pos)
    theta = (360/(2*np.pi)*atan2(dart_pos[0], dart_pos[1]))%360
    
    # number section
    segment_values = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5, 20]
    number = segment_values[int((theta + 9)//18)]
    
    # bonus
    if r <= 6.35:
        score = 50
    elif 6.35 < r <= 15.9:
        score = 25
    elif r > 170:
        score = 0
    elif 162 < r <= 170:
        score = 2*number
    elif 99 < r <= 107:
        score = 3*number
    else:
        score = number
                   
    return score

def expected_score(target, sigma, N):
    average = 0
    for n in range(N):
        average += score(throw(target, sigma))/N
    return average