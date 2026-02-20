Problem: Reverse List
Pattern: Array Traversal (Reverse Index)


Approach:
- Create empty list
- Traverse original list backwards
- Append elements to new list
- Return reversed list

Time Complexity: O(n)
Space Complexity: O(n)


def reverse_list(nums):
    reversed_list = []

    for i in range(len(nums) - 1, -1, -1):
        reversed_list.append(nums[i])

    return reversed_list
