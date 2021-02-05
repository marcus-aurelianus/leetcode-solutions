'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''


# reduce time complexity to 0(N2) with pointers and sorting
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j,k = i+1, len(List)-1
            while j<k:
                curr = nums[i]+nums[j]+nums[k]
                if curr==sum:
                    return curr
                if abs(curr-target)<abs(closet-target):
                    closet = curr
                if curr<target:
                    j+=1
                else:
                    k-=1
        return closet
