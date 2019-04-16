# EASY COLLECTION:

# ARRAY

# Remove duplicates from a sorted array in place
def removeDuplicates(nums)
    dedupped_nums = set(nums)
    length = len(nums)
    while length is not 0:
        if nums[0] in dedupped_nums:
            dedupped_nums.remove(nums[0])
            nums.append(nums.pop(0))
            length -= 1
        elif nums[0] not in dedupped_nums:
            nums.pop(0)
            length -= 1
    
    return len(nums)

# Rotate array by k steps to the right
def rotate(nums):
    if k is not 0:
        while k is not 0:
            nums.insert(0, nums.pop())
            k -= 1


# Contains duplicates
def containsDuplicate(nums):
    storage = {}
    for num in nums:
        if num not in storage.keys():
            storage[num] = 1
        else:
            storage[num] += 1
            
    for key, value in storage.items():
        if value > 1:
            return True
    
    return False

# Single number- every element appears twice except for one. Find that single one.
def singleNumber(nums):
    storage = {}
    for num in nums:
        if num not in storage.keys():
            storage[num] = 1
        else:
            storage[num] += 1
    
    for key, value in storage.items():
        if value == 1:
            return key
    
# Intersection of two arrays
def intersect(nums1, nums2):
    result = []
    for num in nums1:
        if num in nums2:
            result.append(num)
            nums2.remove(num)
    
    return result
            
# Plus one- plus one to the integer. The digits are stored such that the most significant
# digit is at the head of the list, and each element in the array contain a single digit.
def plusOne(digits):
    string_number = ""
    for number in digits:
        string_number += str(number)
        
    plus_one = int(string_number) + 1
    
    result = []
    for item in str(plus_one):
        result.append(int(item))
        
    return result

# Move zeros- move all zeros to the end of array and keep order of the rest (in place)
def moveZeroes(nums):
    zeros = []
    length = len(nums)
    while length is not 0:
        if nums[0] == 0:
            nums.pop(0)
            zeros.append(0)
        else:
            nums.append(nums.pop(0))
        length -= 1
        
    nums.extend(zeros)

# Two sum- indices of numbers that sum to target
def twoSum(nums, target):
    result = []
    for index_one in range(len(nums)):
        number_to_find = target - nums[index_one]
        for index_two in range(len(nums)- 1):
            if index_two != index_one:
                if nums[index_two] == number_to_find:
                    result.append(index_one)
                    result.append(index_two)
                    
                    return result

# Rotate image- You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise). (in place
def rotate(matrix):
    original_length = len(matrix)
    counting_length = len(matrix)
    last_line = []
    while counting_length > 0:
        for index, list_of_numbers in enumerate(matrix):
            if counting_length == original_length: #meaning first loop to take them all 
                last_line.insert(0, list_of_numbers.pop(0))
            elif index <= original_length - 1 :
                last_line.insert(0, list_of_numbers.pop(0))
        matrix.append(last_line)
        counting_length -= 1
        last_line = []
    
    while original_length > 0:
        del matrix[0]
        original_length -= 1)
                    
                
    