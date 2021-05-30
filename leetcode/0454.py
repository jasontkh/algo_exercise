class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        result_to_count = {}
        for i in nums1:
            for j in nums2:
                temp_ans = i + j
                if temp_ans in result_to_count:
                    result_to_count[temp_ans] += 1
                else:
                    result_to_count[temp_ans] = 1

        # Prepare for final result
        number_of_solutions = 0
        for k in nums3:
            for l in nums4:
                temp = -l - k
                if temp in result_to_count:
                    number_of_solutions += result_to_count[temp]

        return number_of_solutions