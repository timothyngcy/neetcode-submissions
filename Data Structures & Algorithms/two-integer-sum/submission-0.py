class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum_dict = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in two_sum_dict:
                return [two_sum_dict[diff], i]
            else: 
                two_sum_dict[nums[i]] = i





