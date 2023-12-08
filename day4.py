from main import read_input


def score_cards(current_card_idx, card, scores):
    scores[current_card_idx] += 1

    winning_numbers = set(card[card.find(':') + 2:card.find('|') - 1].split())
    selected_numbers = set(card[card.find('|') + 2:].split())
    num_matching_nums = len(winning_numbers.intersection(selected_numbers))

    for j in range(num_matching_nums):
        scores[current_card_idx + j + 1] += scores[current_card_idx]

    return num_matching_nums


if __name__ == '__main__':
    lines = read_input('/Users/dallenmn/PycharmProjects/adventOfCode2023/inputs/day4.txt')

    cards = [0] * len(lines)
    for i in range(len(lines)):
        score_cards(i, lines[i], cards)

    answer = sum(cards)
    print(answer)
