#Find the largest no from the list
nums = [12, 45, 7, 89, 34]
largest=nums[0] #assuming that first no is the largest in the list

for i in nums: # for each iteration of no i in the list nums
    if i >largest: # if no i is > nums[0] or 12 then largest no is i now else run next iteration.
        largest=i
print("largset no is ",largest)