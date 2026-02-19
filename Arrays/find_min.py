Problem: Find Minimum in Array
Pattern: Array Traversal

Approach:
- Assume first element is minimum
- Traverse list
- Update min when smaller element found

Time Complexity: O(n)
Space Complexity: O(1)


def find_min(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num
