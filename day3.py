from main import read_input


def create_engine_schematic(lines):
    temp = []
    for line in lines:
        temp.append([cell for cell in line.rstrip()])
    return temp


def is_gear(schematic, row, col):
    return schematic[row][col] == '*'


def is_out_of_bounds(search_r, search_c, schematic):
    return not 0 <= search_r < len(schematic) or not 0 <= search_c < len(schematic[0])


def find_number(schematic, search_r, search_c):
    number = schematic[search_r][search_c]

    # search left
    left_c = search_c - 1
    while left_c >= 0:
        if schematic[search_r][left_c].isnumeric():
            number = schematic[search_r][left_c] + number
            left_c -= 1
        else:
            break

    # search right
    right_c = search_c + 1
    while right_c < len(schematic[0]):
        if schematic[search_r][right_c].isnumeric():
            number = number + schematic[search_r][right_c]
            right_c += 1
        else:
            break

    return int(number)


def solve_puzzle(schematic):
    total = 0

    for row in range(len(schematic)):
        for col in range(len(schematic[0])):
            nums_near = []

            if not is_gear(schematic, row, col):
                continue

            # top row
            try:
                if schematic[row - 1][col].isnumeric():
                    nums_near.append(find_number(schematic, row - 1, col))
                else:
                    if schematic[row - 1][col - 1].isnumeric():
                        nums_near.append(find_number(schematic, row - 1, col - 1))
                    if schematic[row - 1][col + 1].isnumeric():
                        nums_near.append(find_number(schematic, row - 1, col + 1))
            except IndexError:
                pass

            # center row
            if schematic[row][col - 1].isnumeric():
                nums_near.append(find_number(schematic, row, col - 1))
            if schematic[row][col + 1].isnumeric():
                nums_near.append(find_number(schematic, row, col + 1))

            # bottom row
            try:
                if schematic[row + 1][col].isnumeric():
                    nums_near.append(find_number(schematic, row + 1, col))
                else:
                    if schematic[row + 1][col - 1].isnumeric():
                        nums_near.append(find_number(schematic, row + 1, col - 1))
                    if schematic[row + 1][col + 1].isnumeric():
                        nums_near.append(find_number(schematic, row + 1, col + 1))
            except IndexError:
                pass

            if len(nums_near) == 2:
                total += nums_near[0] * nums_near[1]

    return total


if __name__ == '__main__':
    input_lines = read_input('/Users/dallenmn/PycharmProjects/adventOfCode2023/inputs/day3.txt')
    engine_schematic = create_engine_schematic(input_lines)
    answer = solve_puzzle(engine_schematic)
    print(answer)
