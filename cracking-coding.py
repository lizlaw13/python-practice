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

    if len(storage_one) > len(storage_two):
        for key, value in storage_two.items():
            if key not in storage_one and value not in storage_one:
                return False
            return True

    else:
        for key, value in storage_one.items():
            if key not in storage_two and value not in storage_two:
                return False
            return True

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
