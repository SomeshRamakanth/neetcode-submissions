import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]

        target = len(nums) - k  # kth largest = target index in sorted ascending order

        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]

            # 3-way partition:
            # nums[left:lt] < pivot
            # nums[lt:i] == pivot
            # nums[gt+1:right+1] > pivot
            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            if target < lt:
                right = lt - 1
            elif target > gt:
                left = gt + 1
            else:
                return nums[target]