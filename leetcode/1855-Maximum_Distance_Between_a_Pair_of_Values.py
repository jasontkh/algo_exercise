from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        current_max = 0

        for i in range(len(nums1)):
            for j in range(current_max + i + 1, len(nums2)):
                if nums2[j] >= nums1[i]:
                    current_max = j - i
                else:
                    break

        return current_max


nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]

ans = Solution().maxDistance(nums1, nums2)
print(ans)