class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        zero_idx = -1

        for i in range(len(nums)):
            num = nums[i]

            if num != 0:
                total_product *= num
            else:
                zero_count += 1
                zero_idx = i
            
            if zero_count == 2:
                return [0] * len(nums)
        
        if zero_count == 1:
            product_list = [0] * len(nums)
            product_list[zero_idx] = total_product
            return product_list

        product_list = []

        for num in nums:
            if num != 0:
                product_list.append(int(total_product/num))
            else:
                product_list.append(0)

        return product_list