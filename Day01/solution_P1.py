'''
--- Day 1: Trebuchet?! ---

---------------------------
[Part 1]
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

---------------------------
# My approach:

1. Initialize a variable, SUM, to store the sum
2. Read the file line by line, for each line:
    1. Extract the first and last digit of each line
    2. SUM = SUM + 10*first_digit + last_digit
'''

def sum_digits(file):
    # initialize variable to store sum
    SUM = 0

    # open file
    with open(file, 'r') as f:
        # read file line by line
        for line in f:
            # find list of digits in line
            digits = [x for x in line if x.isdigit()]

            # extract first and last digit
            first_digit = int(digits[0])
            last_digit = int(digits[-1])

            # add to sum
            SUM += 10*first_digit + last_digit

    # print sum
    return(SUM)



# test_file = 'test_P1.txt'
# print(sum_digits(test_file))

input_file = 'input.txt'
print(sum_digits(input_file))

