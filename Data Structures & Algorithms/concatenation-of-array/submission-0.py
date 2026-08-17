class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 2 * len(nums) 
        ans = [0] * n
        for i in range(n) :
            if i >= (len(nums)) :
                ans[i] = nums[i%len(nums)]
            else :
                ans[i] = nums[i]

        return ans

