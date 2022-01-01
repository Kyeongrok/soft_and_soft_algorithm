def solution(nums):
    result = 0
    for n in nums:
        if n > result:
            result = n
        print(result)

    return result

print(solution([9, 22, 7,3,  4, 5, 23]))
