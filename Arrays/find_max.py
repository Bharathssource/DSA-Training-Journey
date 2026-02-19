

Problem: Find Maximum in Array

Approach:
- Assume first element is max
- Traverse list
- Update max if larger element found

Time Complexity: O(n)
Space Complexity: O(1) 


def find_max(nums):
  max_num = nums[0]
  for num in nums:
    if nums > max_num:
        max_num = nums
return max_num

