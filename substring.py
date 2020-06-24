# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:57:32 2020

@author: ved67
"""


"""
program for finding the longest substring arranged in alphabetical order in a string
"""
s =input("Enter a string: ")
before=ord(s[0])
start=0
len1=0
end=0
string=s[0]
for i in range(1, len(s), 1):
    if ord(s[i])>=  before:
        end= end + 1
        if end-start > len(string)-1:
           string = ""
           for j in range(start, end+1):
               string = string + s[j]
    else:
       start = i 
       end=i
    before=ord(s[i])
print("Longest substring in alphabetical order is:" + string)