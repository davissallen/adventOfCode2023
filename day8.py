import math
import re


def convert_line_to_coordinate(line, memo):
    pattern = r'(\w{3}) = \((\w{3}), (\w{3})\)'
    match = re.match(pattern, line)
    location, left, right = match.group(1), match.group(2), match.group(3)
    memo[location] = {
        'L': left,
        'R': right,
    }


def solve_part_one(_directions, _desert_map):
    answer = 0
    current_location = 'AAA'
    while current_location != 'ZZZ':
        next_move = _directions[answer % len(_directions)]
        current_location = _desert_map[current_location][next_move]
        answer += 1
    print(answer)


def solve_part_two_slow(_directions, _desert_map):
    answer = 0

    current_locations = [loc for loc in _desert_map.keys() if loc[-1] == 'A']

    while not all(loc[-1] == 'Z' for loc in current_locations):
        next_move = _directions[answer % len(_directions)]
        new_locations = []
        for location in current_locations:
            new_locations.append(_desert_map[location][next_move])
        current_locations = new_locations
        answer += 1
    print(answer)


def solve_part_two_faster(_directions, _desert_map):
    starting_locations = [loc for loc in _desert_map.keys() if loc[-1] == 'A']
    memo = {loc: dict() for loc in starting_locations}

    for starting_location in starting_locations:
        next_location = starting_location
        count = 0
        while next_location not in memo[starting_location]:
            if next_location in memo[starting_location]:
                # been here before, stop processing
                break

            if next_location[-1] == 'Z':
                memo[starting_location][next_location] = count

            next_location = _desert_map[next_location][_directions[count % len(_directions)]]
            count += 1

    if not all(len(memo[location]) == 1 for location in memo.keys()):
        return  # bad assumption

    ints = [[i for i in x.values()][0] for x in memo.values()]
    print(math.lcm(*ints))


if __name__ == '__main__':
    lines = open('/Users/dallenmn/PycharmProjects/adventOfCode2023/inputs/day8.txt').read().split('\n')
    directions = [letter for letter in lines[0]]

    desert_map = dict()
    for idx in range(2, len(lines)):
        convert_line_to_coordinate(lines[idx], desert_map)

    solve_part_two_faster(directions, desert_map)
