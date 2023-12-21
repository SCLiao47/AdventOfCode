'''
--- Day 1: Trebuchet?! ---

---------------------------
[Part 1]


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

