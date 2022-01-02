def min_idx(nums):
    result = 0
    for i in range(1, len(nums)):
        print(nums[i])
        if nums[result] > nums[i]:
            result = i
    return result


print(min_idx([-9, -22, -3, -5, -7, -10]))


