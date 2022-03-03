#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 10:12:10 2022

@author: prateek
"""
import os
import cv2
import glob

for filename in glob.glob(r'/home/prateek/Desktop/inputs/*.jpg'):
    print(filename)
    img=cv2.imread(filename) 
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'/home/prateek/Desktop/outputs/{os.path.basename(filename)}', gray_image)