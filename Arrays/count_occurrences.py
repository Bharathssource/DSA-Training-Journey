Problem: Count Occurrences in Array
Pattern: Array Traversal + Accumulator


Approach:
- Initialize counter = 0
- Traverse list
- Increment counter when element equals target

Time Complexity: O(n)
Space Complexity: O(1)


def count_occurrences(nums, target):
    counter = 0
    for num in nums:
        if num == target:
            counter += 1
    return counter
