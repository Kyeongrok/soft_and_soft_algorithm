def max(nums):
    result = nums[0]
    for n in nums[1:]:
        print('n', n)
        if n > result:
            result = n

    return result

print(max([-9, -22, -7, -3, -4, -5, -23]))
