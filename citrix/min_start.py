#!/bin/python

import math
import os
import random
import re
import sys



def minStart(arr):
    """
    there should be a range in which we should search for x it should be
    in based on sum of the array
    if sum is positive -sum to sum+1 should be the range
    """
    min_value = 1 - (min(arr) - 1)
    max_value = sum(arr) + 1
    # print "min_value:{} max_value:{}".format(min_value, max_value)
    lower_limit = min_value if max_value > min_value else max_value
    upper_limit = min_value if min_value > max_value else min_value
    result = None
    # print "lower_limit:{} upper_limit:{}".format(lower_limit, upper_limit)
    for i in range(lower_limit, 1000000+1):
        x = i
        valid_value = False
        for each in arr:
            running_sum = x + each
            if running_sum < 1:
                valid_value = False
                break
            else:
                valid_value = True
                x = running_sum
        if valid_value is True:
            result = i
            break
    return result



if __name__ == '__main__':
    arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]  #-> -17, 13
    arr1 = [-5, 4, -2, 3, 1]  # -7, 8
    arr2 = [3, -6, 5, -2, 1]  # -8, 9
    arr3 = [-4, 3, 2, 1]  # -4, 6
    arr4 = [-23457, -2374, 1, 23489, 19283]  # -25831, 42773
    arr5 = [234578, 34567, 789350]  # 0, 1058495
    arr6 = [-237652, -141413, -141412]  #-520477, 0
    print minStart(arr), minStart(arr) == 8, min(arr), max(arr), sum(arr)
    print minStart(arr1), minStart(arr1) == 6, min(arr1), max(arr1), sum(arr1)
    print minStart(arr2), minStart(arr2) == 4, min(arr2), max(arr2), sum(arr2)
    print minStart(arr3), minStart(arr3) == 5, min(arr3), max(arr3), sum(arr3)
    print minStart(arr4), minStart(arr4) == 25832, min(arr4), max(arr4), sum(arr4)
    print minStart(arr5), minStart(arr5) == -34565, min(arr5), max(arr5), sum(arr5)
    print minStart(arr6), minStart(arr6) == 520478, min(arr6), max(arr6), sum(arr6)
