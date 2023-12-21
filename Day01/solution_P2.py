'''
--- Day 1: Trebuchet?! ---

---------------------------
[Part 2]
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

---------------------------
# My approach:

1. Initialize a variable, SUM, to store the sum
2. Read the file line by line, for each line:
    1. Change all words to digits
    2. Extract the first and last digit of each line
    3. SUM = SUM + 10*first_digit + last_digit
'''

import re

def getdigits(line):
    '''
    check if digits are either spelled out with letters or in actual digits
    return a matrix of such case, each row is (start_index, end_index, digit)
    if no such case, return empty matrix
    '''
    # initialize dictionary to store digit pairs
    digit_pairs = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    # initialize list to store results
    digits = []

    # iterate over each digit pair
    for digit, value in digit_pairs.items():
        for m in re.finditer(digit, line):
            digits.append((m.start(), m.end(), int(value)))

    # check if digits in actual digits are in line
    for idx, value in enumerate(line):
        # print(idx, value)
        if value.isdigit():
            digits.append((idx, idx+1, int(value)))

    # sort the rows of the matrix by start_index
    digits = sorted(digits, key=lambda x: x[0]) 

    return digits


def sum_digits(file):
    # initialize variable to store sum
    SUM = 0

    # open file
    with open(file, 'r') as f:
        # read file line by line
        for line in f:
            # change words to digits
            digits = getdigits(line)

            # extract first and last digit
            first_digit = digits[0][2]
            last_digit = digits[-1][2]

            # add to sum
            SUM += 10*first_digit + last_digit

    # return sum
    return SUM


test_file = 'test_P2.txt'
print(sum_digits(test_file))

input_file = 'input.txt'
print(sum_digits(input_file))