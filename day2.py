import functools
import re
from main import read_input


# max_num_dice = {
#     'red': 12,
#     'green': 13,
#     'blue': 14,
# }


def parse_game(game):
    match = re.search(r'Game (\d+): (.*)', game)
    game_id, round_results = match.group(1), match.group(2).split(';')

    max_counts = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for round_result in round_results:
        rolls = round_result.split(',')
        for roll in rolls:
            match = re.search(r'\s*(\d+) (\w+)', roll)
            count, color = match.group(1), match.group(2)
            max_counts[color] = max(max_counts[color], int(count))

    return int(game_id), max_counts


def score_game(game):
    game_id, game_results = parse_game(game)
    return functools.reduce(lambda a, b: a*b, game_results.values())


if __name__ == '__main__':
    games = read_input('/Users/dallenmn/PycharmProjects/adventOfCode2023/inputs/day2.txt')
    answer = sum(score_game(game) for game in games)
    print(answer)
