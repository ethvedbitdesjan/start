# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:54:20 2020

@author: ved67
"""
s = input("Enter a string: ")
count=0
for char in s:
    if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
        count= count + 1
print(count)


