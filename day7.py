from collections import Counter


card_ranks = {
    'A': 'a',
    'K': 'b',
    'Q': 'c',
    # 'J': 'd',
    'T': 'e',
    '9': 'f',
    '8': 'g',
    '7': 'h',
    '6': 'i',
    '5': 'j',
    '4': 'k',
    '3': 'l',
    '2': 'm',
    'J': 'n',
}


def is_five_of_a_kind(card_freq):
    return len(card_freq) == 1


def is_four_of_a_kind(card_freq):
    return len(card_freq) == 2 and any(freq for freq in card_freq.values() if freq == 4)


def is_full_house(card_freq):
    return len(card_freq) == 2 and any(freq for freq in card_freq.values() if freq == 3)


def is_three_of_a_kind(card_freq):
    return any(freq for freq in card_freq.values() if freq == 3)


def is_two_pair(card_freq):
    return len(card_freq) == 3 and len([freq for freq in card_freq.values() if freq == 2]) == 2


def is_one_pair(card_freq):
    return any(freq for freq in card_freq.values() if freq == 2)


def convert_jokers(card_freq):
    """Find the most frequent card, and convert all Js to that."""
    if 'J' not in card_freq:
        return card_freq

    most_frequent_card = sorted(card_freq.items(), key=lambda x: (-x[1], card_ranks[x[0]]))[0][0]
    num_js = card_freq['J']
    del card_freq['J']

    if most_frequent_card == 'J':
        if num_js == 5:
            return {'A': 5}
        most_frequent_card = sorted(card_freq.items(), key=lambda x: (-x[1], card_ranks[x[0]]))[0][0]

    card_freq[most_frequent_card] += num_js
    return card_freq


def rank_hand(hand):
    new_hand_freq = convert_jokers(Counter(hand))

    ranking = []
    if is_five_of_a_kind(new_hand_freq):
        ranking.append('a')
    elif is_four_of_a_kind(new_hand_freq):
        ranking.append('b')
    elif is_full_house(new_hand_freq):
        ranking.append('c')
    elif is_three_of_a_kind(new_hand_freq):
        ranking.append('d')
    elif is_two_pair(new_hand_freq):
        ranking.append('e')
    elif is_one_pair(new_hand_freq):
        ranking.append('f')
    else:
        ranking.append('g')

    for c in hand:
        ranking.append(card_ranks[c])

    return ''.join(ranking)


def solve(hands):
    hands.sort(key=lambda x: rank_hand([c for c in x[0]]))
    total = idx = 0
    while idx < len(hands):
        bid = int(hands[idx][1])
        rank = len(hands) - idx
        total += bid * rank
        idx += 1
    return total


if __name__ == '__main__':
    lines = open('/Users/dallenmn/PycharmProjects/adventOfCode2023/inputs/day7.txt').read().split('\n')
    hands = [s.split() for s in lines]
    answer = solve(hands)
    print(answer)
