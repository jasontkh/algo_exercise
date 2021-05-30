from bisect import bisect_left

# nums1 = [101,102,103]
nums1 = [1,2]

nums2 = [3]

if len(nums1) == 0 or len(nums2) == 0:
    nums3 = nums1 + nums2
    if len(nums3) % 2 ==0:
        print("ANS:", (nums3[(len(nums3) - 1)//2] + nums3[len(nums3)//2])/2)
    else:
        print("ANS:", nums3[len(nums3) // 2])
target_position = (len(nums1) + len(nums2) - 1) // 2
is_even = (len(nums1) + len(nums2)) % 2 == 0
print(is_even)

low, high = 0, len(nums2)
while low < high:
    mid = low + (high - low) // 2

    nums1_insertion_position = bisect_left(nums1, nums2[mid])
    array_value = mid + nums1_insertion_position

    if array_value < target_position:
        low = mid + 1
    elif array_value > target_position:
        high = mid
    else:
        if is_even:
            smaller = nums2[mid]
            candidates = []
            if mid < len(nums2) - 1:
                candidates.append(nums2[mid + 1])
            if nums1_insertion_position < len(nums1):
                candidates.append(nums1[nums1_insertion_position])

            larger = min(candidates)

            print("ANS:", (smaller + larger)/2)
        else:
            print("ANS:", nums2[mid])
        break

# Describe the pointer `low`
median_is_at = low

if median_is_at == 0:
    if is_even:
        smaller = nums1[target_position]
        candidates = [nums2[0]]
        if target_position + 1 < len(nums1):
            candidates.append(nums1[target_position + 1])
        larger = min(candidates)
        print("ANS_e:", (smaller + larger) / 2)
    else:
        print("ANS_f:", nums1[target_position])
elif median_is_at == len(nums2):
    if is_even:
        print("ANS_z:", (nums1[target_position - len(nums2)] + nums1[target_position - len(nums2)+1]) / 2)
    else:
        print("ANS_y:", nums1[target_position - len(nums2)])
else:
    nums1_insertion_position = bisect_left(nums1, nums2[low])
    merged_position = low + nums1_insertion_position
    exceeded_position = merged_position - target_position
    if is_even:
        smaller = nums1[nums1_insertion_position - exceeded_position]
        candidates = [nums2[median_is_at]]
        if nums1_insertion_position - exceeded_position + 1 < len(nums1):
            candidates.append(nums1[nums1_insertion_position - exceeded_position + 1])
        larger = min(candidates)
        print("ANS_g:", (smaller + larger) / 2)
    else:
        print("ANS_w:", nums1[nums1_insertion_position - exceeded_position])
