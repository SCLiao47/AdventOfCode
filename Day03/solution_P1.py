'''
Day 3: Gear Ratios
'''

'''
[Part 1: What is the sum of all of the part numbers in the engine schematic?]

My approach:
1. Read the input as a matrix of characters
2. Get active digits
    - Create a mask Ms_ori for symbols and dilate it to get the mask Ms
    - Create a mask Md_ori for digits
    - Take the intersection of Ms and Md_ori to get the mask Ma
    - Get the mask Md for actual number from the Md_ori by connected components with seed points in Ma
3. Get all the numbers
    - create a char matrix with active digits and all other elements being '.'
    - for each line, split the array by '.' and get the numbers
    - add the numbers to a list
4. Sum up all the numbers

'''

def get_active_digits(input):
    # Get size of the input
    nrow = len(input)
    ncol = len(input[0])

    # Create a mask Ms_ori for symbols and a mask Md for digits
    Ms_ori = [[False] * ncol for _ in range(nrow)]
    Md_ori = [[False] * ncol for _ in range(nrow)]
    for i in range(nrow):
        for j in range(ncol):
            if input[i][j] not in ['.']:
                if input[i][j].isdigit():
                    Md_ori[i][j] = True
                else:
                    Ms_ori[i][j] = True

    # Dilate Ms_ori to get the mask Ms
    Ms = [[False] * ncol for _ in range(nrow)]
    for i in range(nrow):
        for j in range(ncol):
            if Ms_ori[i][j]:
                if i == 0:
                    idx_r = [0, 1]
                elif i == nrow-1:
                    idx_r = [nrow-2, nrow-1]
                else:
                    idx_r = [i-1, i, i+1]

                if j == 0:
                    idx_c = [0, 1]
                elif j == ncol-1:
                    idx_c = [ncol-2, ncol-1]
                else:
                    idx_c = [j-1, j, j+1]

                for r in idx_r:
                    for c in idx_c:
                        Ms[r][c] = True

    # Take the intersection of Ms and Md_ori to get the mask Ma
    Ma = [[Ms[i][j] and Md_ori[i][j] for j in range(ncol)] for i in range(nrow)]

    # Get the mask Md for actual number from the Md_ori by connected components with seed points in Ma
    # Get the seed points in Ma
    seed = []
    for i in range(nrow):
        for j in range(ncol):
            if Ma[i][j]:
                seed.append((i, j))

    # Use seed points to get the mask Md
    Md = [[False] * ncol for _ in range(nrow)]
    for s in seed:
        r = s[0]
        c = s[1]

        # Get the connected components
        # Use a queue to store the points to be checked
        queue = [c]
        while len(queue) > 0:
            # Get the first point in the queue
            p = queue.pop(0)

            # Get the indices of the points to be checked
            if p == 0:
                idx_c = [0, 1]
            elif p == ncol-1:
                idx_c = [ncol-2, ncol-1]
            else:
                idx_c = [p-1, p, p+1]

            # Check the points
            for c in idx_c:
                if Md_ori[r][c] and not Md[r][c]:
                    Md[r][c] = True
                    queue.append(c)

    return Md


def process_input(file_name):
    # Read the input as a matrix of characters
    with open(file_name, 'r') as f:
        input = [list(line.strip()) for line in f.readlines()]

    # Get size of the input
    nrow = len(input)
    ncol = len(input[0])

    # Get active digits
    Md = get_active_digits(input)

    # Get all the numbers
    # Create a char matrix with active digits and all other elements being '.'
    input_char = [['.' for _ in range(ncol)] for _ in range(nrow)]
    for i in range(nrow):
        for j in range(ncol):
            if Md[i][j]:
                input_char[i][j] = input[i][j]

    numbers = []
    for i in range(nrow):
        line = ''.join(input_char[i])
        line = line.split('.')
        for n in line:
            if n.isdigit():
                numbers.append(int(n))

    # Sum up all the numbers
    return sum(numbers)


test = process_input('test.txt')
print(test)

part1 = process_input('input.txt')
print(part1)

