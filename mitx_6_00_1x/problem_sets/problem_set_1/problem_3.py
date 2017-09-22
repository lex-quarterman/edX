#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:15:29 2017

@author: lex.quarterman
"""
s = 'azcbobobegghakl'
abc_cut = ''
abc_temp = ''
line_break = 0
line_start = 0

for i in range(len(s)-1):  
    if len(abc_temp)> len(abc_cut):
            abc_cut = abc_temp
    if (i+2) < len(s):
        if s[i] > s[i+1] or (i+1) == (len(s)-1): 
           line_break = i+1
           abc_temp = s[line_start:line_break]
           line_start = i+1
    else:
        if s[i]<=s[i+1]:
            line_break = i+2
            abc_temp = s[line_start:line_break]
            line_start = line_break
            if len(abc_temp)> len(abc_cut):
                abc_cut = abc_temp
                print(abc_cut)
        else:
            line_break = i+1
            abc_temp = s[line_start:line_break]
            line_start = line_break
            if len(abc_temp)> len(abc_cut):
                abc_cut = abc_temp
    
print("Longest substring in alphabetical order is:",abc_cut)
        