# Wave Array
# Difficulty: EasyAccuracy: 63.69%Submissions: 256K+Points: 2
# Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place). In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....
# If there are multiple solutions, find the lexicographically smallest one.

# Note: The given array is sorted in ascending order, and you don't need to return anything to change the original array.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [2, 1, 4, 3, 5]
# Explanation: Array elements after sorting it in the waveform are 2, 1, 4, 3, 5.

from typing import List


class Solution:
    def convertToWave(self, arr : List[int]) -> None:
        n = len(arr)
        for i in range(0,n-1,2):
            arr[i],arr[i+1] = arr[i+1],arr[i]
        return arr