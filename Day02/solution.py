'''
--- Day 2: Cube Conundrum ---
----------------------
# My approach
1. Data processing: Read the input file line by line
    1. Split the line into two parts: game id and playouts
    2. Further split the playouts into reveal as tuples of number for each color (red, green, blue)
    3. Comptue the maximum number of cubes for each color across all palayouts
    4. Store the game id and the maximum number of cubes for each color in a dictionary
2. [Part 1] Compare the maximum number of cubes for each color in the dictionary with the given number of cubes for each color
3. [Part 2] Compute the power of cubes for each color in the dictionary

'''

import numpy as np

# def get_max_cubes(reveal):

def playouts_to_reveal(playouts_text):
    '''
    Process the playouts and return a list of tuples of number of cubes for each color
    '''
    reveals = playouts_text.split(';')

    playouts = np.zeros((len(reveals), 3))
    
    for i, reveal in enumerate(reveals):
        reveal = reveal.split(',')
        # print(reveal)

        # check the color for each reveal
        red = 0
        green = 0
        blue = 0
        for color in reveal:
            if color.find('red') != -1:
                red = int(color.split(' ')[1])

            if color.find('green') != -1:
                green = int(color.split(' ')[1])
            
            if color.find('blue') != -1:
                blue = int(color.split(' ')[1])

            # print(color, red, green, blue)

        playouts[i, 0] = red
        playouts[i, 1] = green
        playouts[i, 2] = blue

        # print(playouts)

    return playouts

def process_data(file):
    # Read the input file
    with open(file, 'r') as f:
        data = f.readlines()

        # split the line into game id and playouts
        allGame_text = [line.split(':') for line in data]

        allGame_maxColor = np.zeros((len(allGame_text), 3))

        for idx, game in enumerate(allGame_text):
            playouts_text = game[1]

            playout = playouts_to_reveal(playouts_text)
            # print(playout)

            # compute the maximum number of cubes for each color
            max_cubes = np.max(playout, axis=0)

            # store the game id and the maximum number of cubes for each color in a dictionary
            allGame_maxColor[idx, :] = max_cubes

            # print(allGame_maxColor)
            # print(allGame_maxColor.shape)
    return allGame_maxColor

def func_sol1(file, config):
    # process the data
    allGame_maxColor = process_data(file)

    # compare the maximum number of cubes for each color in the dictionary with the given number of cubes for each color
    mask_ture = np.all(allGame_maxColor <= config, axis=1)

    sum = 0
    for idx, mask in enumerate(mask_ture):
        if mask == True:
            sum += idx + 1

    return sum

def func_sol2(file, config):
    # process the data
    allGame_maxColor = process_data(file)

    # compute the power of cubes for each color in the dictionary
    power = np.prod(allGame_maxColor, axis=1)

    return np.sum(power)


# Test
test_file = 'test.txt'
test_config = [12, 13, 14]

sol1_test = func_sol1(test_file, test_config)
sol2_test = func_sol2(test_file, test_config)
print(sol1_test, sol2_test)

# actual data
file = 'input.txt'
config = [12, 13, 14]

sol1 = func_sol1(file, config)
sol2 = func_sol2(file, config)
print(sol1, sol2)