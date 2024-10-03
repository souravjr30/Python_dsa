def reaching(nums):
    reach = 0
    for i in range(len(nums)):
        if i > reach:
            return False
        reach = max(reach, i+nums[i])

        if reach >= (len(nums)-1):
            return True
    return False



nums = [3,2,1,0,4]
if reaching(nums) == True:
    print("Yes")
else:
    print("False"
          
          
          
'''
given an array of intergers where each element represents the maximum number of indices that can be jumped forward from that position.write a program to check if you can reach the last element of the array starting from the first
'''