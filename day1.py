import re

from main import read_input

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
}


def get_code_from_line(line):
    if not line:
        return 0

    idx = 0
    nums = []
    while idx < len(line):
        for digit in digits.keys():
            if digit == line[idx:idx + len(digit)]:
                nums.append(digits[digit])
                idx += 1
                break
            else:
                continue
        else:
            idx += 1

    return int(nums[0] + nums[-1])


if __name__ == '__main__':
    lines = read_input('/Users/dallenmn/PycharmProjects/adventOfCode2023/inputs/day1.txt')
    answer = sum(get_code_from_line(line) for line in lines)
    print(answer)
