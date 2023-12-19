def find_starting_location(_maze):
    for row in range(len(_maze)):
        for col in range(len(_maze[0])):
            if _maze[row][col] == 'S':
                return row, col
    raise IOError("can't find the start")


def is_out_of_bounds(_maze, row, col):
    return not (0 <= row < len(_maze) and 0 <= col < len(_maze[0]))


def solve_part_one(_maze, _starting_row, _starting_col):
    """
    Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting
    position to the point farthest from the starting position?

    The pipes are arranged in a two-dimensional grid of tiles:
        | is a vertical pipe connecting north and south.
        - is a horizontal pipe connecting east and west.
        L is a 90-degree bend connecting north and east.
        J is a 90-degree bend connecting north and west.
        7 is a 90-degree bend connecting south and west.
        F is a 90-degree bend connecting south and east.
        . is ground; there is no pipe in this tile.
        S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
    """
    max_steps = float('-inf')
    path_chosen = None

    # travel in each 4 directions. if I ever get back to the start, i looped. calc steps
    for row_delta, col_delta, entering_from in [(1, 0, 'north'), (-1, 0, 'south'), (0, 1, 'west'), (0, -1, 'east')]:
        start_direction = entering_from
        memo = [['.'] * len(_maze[0]) for _ in range(len(_maze))]
        row, col = _starting_row + row_delta, starting_col + col_delta
        steps = 0
        while (row, col) != (_starting_row, _starting_col):
            if is_out_of_bounds(_maze, row, col):
                break

            current_pipe = _maze[row][col]
            memo[row][col] = current_pipe
            steps += 1

            if current_pipe == '|':
                if entering_from == 'north':
                    row = row + 1
                elif entering_from == 'south':
                    row = row - 1
                else:
                    break

            elif current_pipe == '-':
                if entering_from == 'east':
                    col = col - 1
                elif entering_from == 'west':
                    col = col + 1
                else:
                    break

            elif current_pipe == 'L':
                if entering_from == 'north':
                    entering_from = 'west'
                    col = col + 1
                elif entering_from == 'east':
                    entering_from = 'south'
                    row = row - 1
                else:
                    break

            elif current_pipe == 'J':
                if entering_from == 'north':
                    entering_from = 'east'
                    col = col - 1
                elif entering_from == 'west':
                    entering_from = 'south'
                    row = row - 1
                else:
                    break

            elif current_pipe == '7':
                if entering_from == 'south':
                    entering_from = 'east'
                    col = col - 1
                elif entering_from == 'west':
                    entering_from = 'north'
                    row = row + 1
                else:
                    break

            elif current_pipe == 'F':
                if entering_from == 'south':
                    entering_from = 'west'
                    col = col + 1
                elif entering_from == 'east':
                    entering_from = 'north'
                    row = row + 1
                else:
                    break

            else:
                break

        if (row, col) == (_starting_row, _starting_col):
            if entering_from == start_direction:
                raise IOError('temp')
            calc_steps = (steps + 1) // 2
            if calc_steps > max_steps:
                max_steps = max(max_steps, calc_steps)
                path_chosen = memo
                # prev direction is entering_from
                ending_direction = {
                    '-'.join(sorted(['north', 'south'])): '|',
                    '-'.join(sorted(['north', 'east'])): 'F',
                    '-'.join(sorted(['north', 'west'])): '7',
                    '-'.join(sorted(['south', 'east'])): 'J',
                    '-'.join(sorted(['south', 'west'])): 'L',
                    '-'.join(sorted(['east', 'west'])): '-',
                }
                path_chosen[_starting_row][_starting_col] = ending_direction['-'.join(sorted([start_direction, entering_from]))]

    return max_steps, path_chosen


def find_contained_cells(_path_chosen):
    _answer = 0
    for row in range(len(_path_chosen)):
        for col in range(len(_path_chosen[row])):
            cell = _path_chosen[row][col]
            if cell != '.':
                continue
            # go down
            count = 0
            prev_pipe = '.'
            for row_idx in range(row, len(_path_chosen)):
                curr_pipe = _path_chosen[row_idx][col]
                if curr_pipe in {'.', '|', 'X'}:
                    continue  # means nothing
                elif curr_pipe == 'L' and prev_pipe == '7':
                    count += 1
                elif curr_pipe == 'J' and prev_pipe == 'F':
                    count += 1
                elif curr_pipe == '-':
                    count += 1
                prev_pipe = curr_pipe
            if count % 2 == 1:
                _path_chosen[row][col] = 'X'
                _answer += 1
    return _answer


def solve_part_two(_maze, _starting_row, _starting_col):
    _, path_chosen = solve_part_one(_maze, _starting_row, _starting_col)

    return find_contained_cells(path_chosen)


if __name__ == '__main__':
    lines = open('/Users/dallenmn/PycharmProjects/adventOfCode2023/inputs/day10.txt').read().split('\n')
    maze = [[letter for letter in line] for line in lines]
    starting_row, starting_col = find_starting_location(maze)
    answer = solve_part_two(maze, starting_row, starting_col)
    print(answer)
