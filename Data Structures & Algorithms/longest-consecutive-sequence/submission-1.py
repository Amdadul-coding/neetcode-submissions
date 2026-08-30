class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print(nums)
        numbers = set(nums)
        longest = 0
        for num in nums:
            if not (num - 1) in numbers:
                length = 0
                while (num + length) in numbers:
                    length += 1
                longest = max(length, longest)
        return longest