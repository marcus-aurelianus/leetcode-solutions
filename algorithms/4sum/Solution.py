'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
 

Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(l,r,target,N,result,results):
            results = []
            for i in range(len(nums)-2):
                l = i + 1; r = len(nums) - 1
                t = target - nums[i]
                if i == 0 or nums[i] != nums[i-1]:
                    while l < r:
                        s = nums[l] + nums[r]
                        if s == t:
                            results.append([nums[i], nums[l], nums[r]])
                            while l < r and nums[l] == nums[l+1]: l += 1
                            while l < r and nums[r] == nums[r-1]: r -= 1
                            l += 1; r -=1
                        elif s < t:
                            l += 1
                        else:
                            r -= 1
            return results        
        
        results = []
        nums.sort()
        for i in range(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]:
                threeResult = threeSum(nums[i+1:], target-nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results
