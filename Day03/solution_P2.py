'''
Day 3: Gear Ratios 
'''

'''
[Part 2: What is the sum of all of the gear ratios in your engine schematic?]

My approach:
1. Read the input as a matrix of characters
2. Get active gears
    - Create a mask Ms_ori for '*' and dilate it to get the mask Ms
    - Create a mask Md_ori for digits
    - Take the intersection of Ms and Md_ori to get the mask Ma
    - Get the mask Md for actual number from the Md_ori by connected components with seed points in Ma
    - verify only 2 numbers per gear
    - store the gear_pair as a list of 2-tuples (gear1, gear2) where gear1 is a list of indices of the first number and gear2 is a list of indices of the second number
3. Get all the gear ratios
    - get the actual number of gear1 and gear2 in gear_pair
    - get the gear ratios by multiplying the numbers
4. Sum up all the numbers


====================================================================================================
[Refelction]
There are much simplier approaches to this problem. 
The main idea is to maintain a matrix, where each element is a list of digits adjecent to a '*'. 
For every element in the list, we check if it is a gear by checking if it has 2 digits (a list of two element).
Then add the gear ratio to the sum.

Technique to do this:
1. scan the input line by line
2. once encounter a digit, maintain a number with list of its indices
3. once the number is complete, check if it is ajenct to a '*'
4. if so, add it to the list of 'gears'
'''

import numpy as np

def get_dilate_row(r, nrow):
    # Get the indices of the rows to be checked
    if r == 0:
        idx_r = [0, 1]
    elif r == nrow-1:
        idx_r = [nrow-2, nrow-1]
    else:
        idx_r = [r-1, r, r+1]

    return idx_r

def get_dilate_col(c, ncol):
    # Get the indices of the columns to be checked
    if c == 0:
        idx_c = [0, 1]
    elif c == ncol-1:
        idx_c = [ncol-2, ncol-1]
    else:
        idx_c = [c-1, c, c+1]

    return idx_c

def get_number(input, seed):
    '''
    Get the actual number for a seed point using connected components
    '''
    # Get size of the input
    nrow = len(input)
    ncol = len(input[0])

    # Get the connected components
    r = seed[0]
    c = seed[1]
    mask = np.zeros(ncol, dtype=bool)

    # Use a queue to store the points to be checked
    queue = [c]
    while len(queue) > 0:
        # Get the first point in the queue
        p = queue.pop(0)

        # Get the indices of the points to be checked
        idx_c = get_dilate_col(p, ncol)

        # Check the points
        for j in idx_c:
            if input[r][j].isdigit() and not mask[j]:
                queue.append(j)
                mask[j] = True

    # Get the actual number
    number = 0
    for j in range(ncol):
        if mask[j]:
            number = number * 10 + int(input[r][j])
    
    return number

def check_gear(mask_star):
    count = 0
    seeds = []
    
    for r in range(3):
        if mask_star[r][0] and mask_star[r][1] and mask_star[r][2]:
            count += 1
            seeds.append((r,1))
        elif mask_star[r][0] and mask_star[r][2]:
            count += 2
            seeds.append((r,0))
            seeds.append((r,2))
        elif mask_star[r][0]:
            count += 1
            seeds.append((r,0))
        elif mask_star[r][2]:
            count += 1
            seeds.append((r,2))
        elif mask_star[r][1]:
            count += 1
            seeds.append((r,1))

    # print(mask_star)
    # print(count)

    if count == 2:
        return True, seeds
    else:
        return False, seeds


def get_gearpair_seed(input):
    # Get size of the input
    nrow = len(input)
    ncol = len(input[0])

    # Create a mask Ms_ori for symbols and a mask Md for digits
    Ms_ori = []
    Md_ori = np.zeros((nrow, ncol), dtype=bool)
    for i in range(nrow):
        for j in range(ncol):
            if input[i][j] == '*':
                Ms_ori.append((i, j))
            if input[i][j].isdigit():
                Md_ori[i][j] = True

    # print(Ms_ori)
    # print(Md_ori)

    # check '*' is a gear and get the seed points
    gear_pairs = []
    for (i,j) in Ms_ori:
        mask_star = np.zeros((3,3), dtype=bool)
        for r in range(-1,2):
            for c in range(-1,2):
                if i+r < 0 or i+r >= nrow or j+c < 0 or j+c >= ncol:
                    continue

                # print(i+r, j+c)

                if Md_ori[i+r][j+c]:
                    mask_star[r+1][c+1] = True
        is_gear, seeds = check_gear(mask_star)
        if is_gear:

            seeds = [(i+s[0]-1, j+s[1]-1) for s in seeds]
            gear_pairs.append((seeds[0], seeds[1]))

    return gear_pairs


def process_input(file_name):
    # Read the input as a matrix of characters
    with open(file_name, 'r') as f:
        input = [list(line.strip()) for line in f.readlines()]

    # Get size of the input
    nrow = len(input)
    ncol = len(input[0])

    # Get active digits
    gearpair_seed = get_gearpair_seed(input)

    gear_ratio = []
    for gear in gearpair_seed:
        # get actual number for each seed
        gear1 = get_number(input, gear[0])
        gear2 = get_number(input, gear[1])

        gear_ratio.append(gear1 * gear2)

    # sum up all the gear ratios
    return sum(gear_ratio)

test = process_input('test.txt')
print(test)

test2 = process_input('test2.txt')
print(test2)

part1 = process_input('input.txt')
print(part1)

