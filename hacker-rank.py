# PROBLEM SOLVING - easy

# Grading Students

# Every student receives a  in the inclusive range from  0 to 100.
# Any  less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's  grade
# according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3,
# round  up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result
# will still be a failing grade.

# Given the initial value of grades for each of Sam's  students,
# write code to automate the rounding process.


def gradingStudents(grades):
    final_grades = []
    for grade in grades:
        if grade % 5 == 0 and grade > 38:
            final_grades.append(grade)
        else:
            grade_copy = grade
            while grade_copy % 5 != 0:
                grade_copy += 1
            if grade_copy - grade < 3 and grade_copy >= 38:
                final_grades.append(grade_copy)
            else:
                final_grades.append(grade)

    return final_grades


# Diagonal Difference

# Given a square matrix, calculate the absolute difference between the sum of its
# diagonals

def diagonalDifference(n, arr):
    right_diagonal = 0
    left_diagonal = 0
    r = n - 1
    l = 0
    for index, numbers in enumerate(arr):
        if index == 0:
            right_diagonal += numbers[-1]
            left_diagonal += numbers[0]
        elif index == len(numbers) - 1:
            right_diagonal += numbers[0]
            left_diagonal += numbers[-1]
        else:
            r -= 1
            right_diagonal += numbers[r]
            l += 1
            left_diagonal += numbers[l]

    return abs(right_diagonal - left_diagonal)


print(diagonalDifference(3, [[11, 2, 4], [4, 5, 6], [10, 8, -12]]))

# Staircase

# Consider a staircase of size n = 4:
   #
  ##
 ###
####

# Observe that its base and height are both equal to n, and the image
# is drawn using # symbols and spaces. The last line is not
# preceeded by any spaces.
# Write a program that prints a staircase of size n.

def staircase(n):
    final_result = []
    i = 1
    i_copy = i
    while i <= n:
        final_result.append([])
        spaces = n - i
        while spaces > 0:
            final_result[i - 1].append(" ")
            spaces -= 1
        while i_copy > 0:
            final_result[i - 1].append("#")
            i_copy -= 1
        i += 1
        i_copy = i 

    for line in final_result:
        print("".join(line))
            
print(staircase(5))

# Bon Appetit 

# Print Bon Appetit if the bill is fairly split. Otherwise, it 
# should print the integer amount of money that Brian owes Anna.

# bonAppetit has the following parameter(s):

# bill: an array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money that Anna contributed to the bill

def bonAppetit(bill, k, b):
    actual_bill = 0
    for index, charge in enumerate(bill):
        if index != k:
            actual_bill += charge

    actual_bill = actual_bill / 2

    if actual_bill == b:
        print("Bon Appetit")
    elif actual_bill != b:
        print(abs(actual_bill - b))
    
print(bonAppetit([3, 10, 2, 9], 1, 12))