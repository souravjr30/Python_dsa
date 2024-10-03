def nums_target(nums, target):
    new_num = []
    for i in range(len(nums)):
        num = nums[i]
        new_num.append((num, i))
    new_num.sort()
    left = 0
    right = len(new_num) - 1

    while left < right:
        current_sum = new_num[left][0] + new_num[right][0]

        if current_sum == target:
            return [new_num[left][1], new_num[right][1]]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return -1


nums = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    nums.append(element)

target = int(input("Enter the target: "))

result = nums_target(nums, target)
print(result)
#python program to return the indices of elements of the array which give sum whose equal to the target