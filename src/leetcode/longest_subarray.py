class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value = nums[0]
        ans = cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > max_value:
                ans = cnt = 1
                max_value = nums[i]
            elif nums[i] < max_value:
                cnt = 0
            elif nums[i] == max_value:
                cnt += 1
            ans = max(cnt, ans)
        return ans