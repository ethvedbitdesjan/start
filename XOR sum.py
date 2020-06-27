# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:02:40 2020

@author: Ethvedbitdesjan
"""
"""
 Prints the value which gives the maximum XOR sum with input value. The 
 output should have maximum k  bits.
"""

def maxXorValue(x, k):
    # Write your code here
    change =0
    ans_string=""
    if k>len(s):
        for i in range(k-len(s)):
            ans_string += "1"
    if k>=len(s):
        for j in range(len(s)):
            if s[j] =="0":
                ans_string +="1"
            else:
                ans_string +="0"
    else:
        for h in range(len(s)):
            if change ==k:
                if len(ans_string)<len(s):
                    for l in range(len(s)-len(ans_string)):
                        ans_string +="0"
                break
            else:
                if s[h]=="0":
                    ans_string +="1"
                    change +=1
                else:
                    ans_string +="0"
    return ans_string
            

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        k = int(input().strip())

        y = maxXorValue(s, k)

        print(str(y)+"\n")

