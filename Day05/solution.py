'''
--- Day 5: If You Give A Seed A Fertilizer ---

[Part 1: What is the lowest location number that corresponds to any of the initial seed numbers?]

My approach:
1. Construct the ordered mapping f() for each source-to-destination pair
    - sort by source number first
    - for each source item k, find corresponding section of the mapping, where S[i] is the begining of the section
    - if k <= S[i] + range[i], then f(k) = D[i] + k - S[i]

    
[Part 2: What is the lowest location number that corresponds to any of the initial seed numbers?]

My approach:
1. For each sorce-to-desstionation, for each source range (start, end), apply each mapping
    - if the seed number is entirely within the range, if not chop the section and append another source range
2. 


'''

def get_seed_P1(line):
    seeds = [int(i) for i in line.split()[1:]]
    seeds.sort()

    return seeds

def get_seed_P2(line):
    line = [int(i) for i in line.split()[1:]]

    seed_ranges = []
    for i in range(0, len(line), 2):
        seed_ranges.append((line[i], line[i]+line[i+1]))

    seed_ranges

    return seed_ranges

def solution_P1(file):
    # read file
    with open(file, 'r') as f:
        lines = f.readlines()

    # # get seed numbers
    sources = get_seed_P1(lines[0])
    # sources = get_seed_P2(lines[0])

    # for each source-to-destination pair, construct the mapping and get the destination number
    mapping = []

    for line in lines[2:]:
        # check utility line
        if ('map' in line):
            # initilize the mapping
            mapping = []

            continue

        elif  line == '\n':            # map the source number to destination number
            # sort the mapping by source number
            mapping.sort(key=lambda x: x[1])
            # print(mapping)
            # print('----------')

            # for each source number, find the destination number
            destinations = []
            idx_mapping = -1
            for k in sources:
                # find the corresponding section
                while idx_mapping+1 < len(mapping) and k >= mapping[idx_mapping+1][1]:
                    idx_mapping += 1
                    # print(idx_mapping)

                fk = k
                # if k <= S[i] + range[i], then f(k) = D[i] + k - S[i]
                if (idx_mapping >= 0) and (idx_mapping < len(mapping)):
                    if k <= mapping[idx_mapping][1] + mapping[idx_mapping][2]:
                        fk = mapping[idx_mapping][0] + k - mapping[idx_mapping][1]
                # print(idx_mapping, ':', k, ' -> ', fk)

                destinations.append(fk)

            sources = destinations
            sources.sort()

        else:
            # read the mapping
            mapping.append([int(i) for i in line.strip().split()])

    # print("=======")
    # print(sources)

    P1 = sources[0]

    return P1

def solution_P2(file):
    # read file
    with open(file, 'r') as f:
        lines = f.readlines()

    # # get seed numbers
    sources_range = get_seed_P2(lines[0])
    New_source = []

    # for each source-to-destination pair, construct the mapping and get the destination number
    for line in lines[2:]:
        # check utility line
        if ('map' in line):
            # initilize the mapping
            New_source = []

            # print('==========', line)
            # print(sources_range)
            # print('----------')

            continue

        elif  line == '\n':       
            sources_range = sources_range + New_source     
            continue

        else:   # apply the mapping
            # read the mapping
            s2d = [int(i) for i in line.strip().split()]

            temp = []

            # print('::::', s2d)
            while len(sources_range) > 0:
                # print(sources_range, '|', New_source)
                (st, ed) = sources_range.pop(0)

                if ed < s2d[1] or st >= s2d[1]+ s2d[2]:
                    # source range remains
                    temp.append((st, ed)) 
                elif st < s2d[1]:
                    if ed < s2d[1] + s2d[2]:
                        # source range is chopped into two
                        temp.append((st, s2d[1]-1))
                        New_source.append((s2d[0], s2d[0] + ed - s2d[1]))
                    else:
                        # Crossing the whole range, source range is chopped into three
                        temp.append((st, s2d[1]-1))
                        New_source.append((s2d[0], s2d[0] + s2d[2]-1))
                        temp.append((s2d[1]+s2d[2], ed))
                else:
                    if ed < s2d[1] + s2d[2]:
                        # all in the range
                        New_source.append((s2d[0] + st - s2d[1], s2d[0] + ed - s2d[1]))

                    else:
                        New_source.append((s2d[0] + st - s2d[1], s2d[0] + s2d[2]-1))
                        temp.append((s2d[1]+s2d[2], ed))

            sources_range = temp
            # print(sources_range, '|', New_source)
            # sources_range = New_source

    # print("=======")
    # print(sources)

    P2 = min(sources_range, key = lambda x: x[0])[0]

    return P2


test_P1 = solution_P1('test.txt')
test_P2 = solution_P2('test.txt')
print(test_P1, test_P2)

sol_P1 = solution_P1('input.txt')
sol_P2 = solution_P2('input.txt')
print(sol_P1, sol_P2)
