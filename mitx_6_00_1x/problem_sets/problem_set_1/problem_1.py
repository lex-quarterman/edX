#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:19:31 2017

@author: lex.quarterman
"""
s = 'azcbobobegghakl'
num_vowels = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        num_vowels +=1
print("Number of vowels: " + str(num_vowels))

