# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:52:38 2020

@author: Ethvedbitdesjan
"""
import sys
def tsp(i,S):
    global matrix
    if len(S) == 1:
        return matrix[i-1][S[0]-1]+matrix[S[0]-1][0]
    else:
        probables=sys.maxsize
        for n in range(len(S)):
            S1 = S.copy()
            S1.pop(n)
            n1 =S[n] 
            probables=min(probables, matrix[i-1][n1-1]+tsp(n1, S1))
        return probables
            
if __name__ == "__main__":
    # matrix contains the distances between the points
    matrix = [[0,10,15,20],
              [5,0,9,10],
              [6,13,0,12],
              [8,8,9,0]]
    ans = tsp(1,[2,3,4])
    print(ans)