# Problem:
# Given an array nums and a target, return indices of the two numbers such that they add up to target.
# Assumption: Exactly one solution exists.
# Approach: Brute-force using nested loops (triangular iteration).
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def twoSum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []
