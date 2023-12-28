'''
Day 4: Scratchcards 
'''

'''
[Part 1: How many points are they worth in total?]

Notation:
- Lw: list of winning numbers
- Ln: list of numbers you have
- N: number of winning numbers
- M: number of numbers you have
- Q: number of matches
- Lc: list of number of copy of each scratchcard

Thougths:
1. Brute force approach: 
    - compare every winning card with every scratchcard. 
    - Time complexity: O(N*M)
2. Sort the winning numbers and the numbers you have, then use two pointers to compare from smallest to largest of winning numbers
    - Time complexity for sorting is O(N*log(N)) + O(M*log(M)) with basic Python sorting (Timsort)
    - use pointers to compare: O(N+M) for worst case

My approach (second thoughts): sort and compare
1. read lines from the input file
2. Data processing
    - split the lines by ':' to get numbers
    - split the lines by '|' to separate winning numbers and numbers you have  
    - convert each list into integers
3. Sort the lists
4. Use two pointers to compare the numbers


Some notes:
1. could potentially improved by checking the largest and smalles number in Lw and Ln, and then only compare the numbers in between. The bounds is O(1) after sorting. 
2. Different implementation should be considered for different input size. Case {N > M} and {N < M} should be considered separately.

====================================================================================================
[Part 2: how many total scratchcards do you end up with?]

My approach:
1. Follow the first part to get the number of matches for each scratchcard
2. Process the matches to get the number of scratchcards using iteration
    - initialize a list of number of copy of each scratchcard Lc by [1,...,1]
    - for i-th card, read number of matches q = Q[i]
        - Lc[(i+1):(i+1+q)] += Lc[i] # add Lc[i] copies of the card to the next q cards
'''

import numpy as np


def process_card(card):
    card = card.rstrip('\n').split(':')[1].split('|')

    Lw = [int(i) for i in card[0].split()]
    Ln = [int(i) for i in card[1].split()]

    # sort the lists
    Lw.sort()
    Ln.sort()

    # print(id, ':', Lw, '|', Ln)
    return Lw, Ln

def get_number_of_matches(Lw, Ln):
    # get the length of the lists
    N = len(Lw)
    M = len(Ln)

    # use two pointers to compare the numbers
    idx_w = 0
    idx_n = 0
    num_matches = 0

    while idx_w < N and idx_n < M:
        if Lw[idx_w] == Ln[idx_n]:
            num_matches += 1
            idx_w += 1
            idx_n += 1
        elif Lw[idx_w] < Ln[idx_n]:
            idx_w += 1
        else:
            idx_n += 1

    return num_matches

def compute_P1(matches):
    score = 0
    for match in matches:
        if match != 0:
            score += 2**(match-1)

    return score

def compute_P2(matches):
    # initialize the list of number of copy of each scratchcard
    Lc = np.ones(len(matches), dtype=int)

    # process the matches
    for i in range(len(matches)):
        q = matches[i]
        if q != 0:
            Lc[(i+1):(i+1+q)] += Lc[i]

    # print(Lc)

    return Lc.sum()


def solution(file_name):
    # Read file
    with open(file_name, 'r') as f:
        cards = f.readlines()

    matches = np.zeros(len(cards), dtype=int)
    for idx_card, card in enumerate(cards):
        # Data processing
        Lw, Ln = process_card(card)

        # get the number of matches
        num_matches = get_number_of_matches(Lw, Ln)

        # store the number of matches
        matches[idx_card] = num_matches
        
    # print(matches)
        
    # compute the scores
    P1 = compute_P1(matches)
    P2 = compute_P2(matches)

    return P1, P2

test1 = solution('test.txt')
print(test1)

sol = solution('input.txt')
print(sol)
