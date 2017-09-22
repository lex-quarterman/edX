#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:03:30 2017

@author: lex.quarterman
"""

s = 'azcbobobegghaklbobob'

num_bob = 0
place_in_s= 0
for char in s:
    if s[place_in_s:place_in_s+3] == 'bob':
        num_bob += 1
    place_in_s += 1
print("Number of times bob occurs is:", num_bob)