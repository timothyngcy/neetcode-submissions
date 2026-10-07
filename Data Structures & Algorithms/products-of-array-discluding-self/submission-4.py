class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp_list = []
        left_product = 1

        for i, num in enumerate(nums):
            lp_list.append(left_product)
            left_product *= num

        rp_list = []
        right_product = 1

        for i, num in reversed(list(enumerate(nums))):
            rp_list.append(right_product)
            right_product *= num

        rp_list = list(reversed(rp_list))

        product_list = []

        for i, num in enumerate(nums):
            left = lp_list[i]
            right = rp_list[i]

            product_list.append(left*right)
        
        return product_list

