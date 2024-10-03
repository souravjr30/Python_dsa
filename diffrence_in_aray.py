def min_steps(nums, x):
    if x < 0:
        return -1

    steps = 0
    while x > 0:
        found = False
        for num in nums:
            if x >= num:
                x -= num
                steps += 1
                found = True
                break
        if not found:
            return -1

    return steps

nums = [1, 1, 4, 2, 3]
x = 5
print(min_steps(nums,x))