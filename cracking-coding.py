# ARRAY AND STRING INTERVIEW QUESTIONS

# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures? 

# >> using dictionary 
def is_unique_with_exta_data_structure(word):
    storage = {}
    for letter in word:
        if letter not in storage.keys():
            storage[letter] = 1
        else:
            storage[letter] += 1
    
    for key, value in storage.items():
        if value is not 1:
            return False
    
    return True

# >> without extra data structures 
def is_unique_no_extra_data_structure(word):
    for index_one, letter_one in enumerate(word):
        for index_two, letter_two in enumerate(word):
            if index_one is not index_two:
                if letter_one == letter_two:
                    return False

    return True

# Write a function to check whether two given strings are permutation of each other or not.
# A permutation of a string is another string that contains same characters, only the 
# order of characters can be different. For example, “abcd” and “dabc” are Permutation of
# each other.

def permutation(word_one, word_two):
    storage_one = {}
    storage_two = {}
    for letter in word_one:
        if letter not in storage_one.keys():
            storage_one[letter] = 1
        else:
            storage_one[letter] += 1
    
    for letter in word_two:
        if letter not in storage_two.keys():
            storage_two[letter] = 1
        else:
            storage_two[letter] += 1

    if storage_one == storage_two:
        return True
    return False

# Write a method to replace all spaces in a string with '%20'
def urlify(url):
    split_url = url.split()
    result = ""
    for index, word in enumerate(split_url):
        if index is not len(split_url) - 1:
            result += word + "%20"
        else:
            result += word
    
    return result

# Given a string, write a function to check if it is a permutation of a palindrome
def permutation_palindrome(word):
    count_no_spaces = 0
    for char in word:
        if char != " ":
            count_no_spaces += 1
    
    storage_no_spaces = {}
    for char in word:
        if char != " ":
            if char not in storage_no_spaces.keys():
                storage_no_spaces[char] = 1
            else:
                storage_no_spaces[char] += 1
    
    one_freq = 0
    two_freq = 0
    total_count = 0

    for key, value in storage_no_spaces.items():
        if value == 1:
            one_freq += 1
            total_count += value
        elif value == 2:
            two_freq += value
            total_count += value

    if count_no_spaces > 4 or count_no_spaces == 3:
        if one_freq == 1 and two_freq == count_no_spaces - 1 and total_count == count_no_spaces:
            return True
        
        return False

    elif count_no_spaces == 4:
        if two_freq == 4:
            return True
        return False

    elif count_no_spaces == 1:
        return True
    
    elif count_no_spaces == 2:
        return False
