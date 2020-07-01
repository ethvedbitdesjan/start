# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:45:56 2020

@author: ved67
"""
"""
 The following code finds the number of inversions in a list of numbers.
 For example: the list - [2,3,8,6,1] has five inversions namely:
     [8,1];[6,1];[8,6];[2,1];[3,1]
Formally an inversion occurs in a list if i<j and list[i]>list[j]
The following code uses modifications in the merge sort algorithm to give
the result. Thus, having the time complexity of O(n log(n))
"""
count=0
def merge(X,Y):
    global count
    X1=0
    Y1=0
    out=[]
    while X1<len(X) and Y1<len(Y):
        if X[X1]<Y[Y1]:
          out.append(X[X1])
          X1 +=1
        else:
          count += (len(X)-X1)
          out.append(Y[Y1])
          Y1 +=1
    out += X[X1:] + Y[Y1:]
    return out
def merge_sort(A):
    mid = len(A)//2
    if len(A)==1:
        return A
    else:
        return merge(merge_sort(A[0:mid]),merge_sort(A[mid:]))
if __name__ == "__main__":
    A = [8,6,1,2,3]
    print(merge_sort(A))
    print(count)