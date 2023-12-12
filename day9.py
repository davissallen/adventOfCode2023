def extrapolate_next_value(_history):
    last_nums_of_each_sequence = []
    current_sequence = [num for num in _history]

    while not all(num == 0 for num in current_sequence):
        # remember
        last_nums_of_each_sequence.append(current_sequence[-1])

        idx = 0
        temp = []
        while idx < len(current_sequence) - 1:
            temp.append(current_sequence[idx + 1] - current_sequence[idx])
            idx += 1
        current_sequence = temp

    num_to_add = 0
    for _ in range(len(last_nums_of_each_sequence)):
        num_to_add += last_nums_of_each_sequence.pop()

    return num_to_add


def solve_part_one(_histories):
    return sum(extrapolate_next_value(history) for history in _histories)


def solve_part_two(_histories):
    return sum(extrapolate_next_value(history[::-1]) for history in _histories)


if __name__ == '__main__':
    lines = open('/Users/dallenmn/PycharmProjects/adventOfCode2023/inputs/day9.txt').read().split('\n')
    histories = [[int(s) for s in line.split()] for line in lines]

    answer = solve_part_two(histories)

    print(answer)
