class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = set()
        for i in nums:
            if i in mp:
                return True
            mp.add(i)
        return False
        