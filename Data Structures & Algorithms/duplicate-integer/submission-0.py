class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        te=set(nums)
        return len(te)!=len(nums)

        