def parse_seeds(input_seeds):
    ranges = []
    for i in range(0, len(input_seeds), 2):
        range_start, range_end = input_seeds[i], input_seeds[i] + input_seeds[i+1]
        ranges.append([range_start, range_end])
    # sorting doesn't matter, but makes debugging easier
    ranges.sort(key=lambda x: x[0])
    return ranges


def parse_mappings(input_mappings):
    parsed_maps = []
    for mapping in input_mappings:
        _mapping = mapping.split('\n')
        __map_name = _mapping[0]  # unused but cool
        parsed_rules = []
        for rule in _mapping[1:]:
            _rule = [int(s) for s in rule.split()]
            start, end, offset = _rule[1], _rule[1] + _rule[2], _rule[0] - _rule[1]
            parsed_rules.append([start, end, offset])

        parsed_rules.sort(key=lambda x: x[0])
        parsed_rules.append([parsed_rules[-1][1], float('inf'), 0])
        if parsed_rules[0][0] != 0:
            parsed_rules.append([0, parsed_rules[0][0], 0])
        parsed_rules.sort(key=lambda x: x[0])

        parsed_maps.append(parsed_rules)
    return parsed_maps


def can_enter_range(left, right, range_start, range_end):
    # 4 overlapping cases:
    #   case1           case2           case3           case4
    #  |----|       |-----|             |------|     |--------|
    # |------|        |------|        |------|        |------|
    case1 = left >= range_start and right <= range_end
    case2 = left <= range_start < right <= range_end
    case3 = range_start <= left < range_end <= right
    case4 = left <= range_start and right >= range_end
    return case1 or case2 or case3 or case4


def are_ranges_overlapped(left, right, map_ranges):
    next_ranges = []
    for range_start, range_end, offset in map_ranges:
        if can_enter_range(left, right, range_start, range_end):
            next_range_start = max(range_start, left) + offset
            next_range_end = min(range_end, right) + offset
            next_ranges.append([next_range_start, next_range_end])
    return next_ranges


def solve_part_two(seed_ranges, maps):
    min_location = float('inf')
    for seed_start, seed_end in seed_ranges:
        current_ranges = [[seed_start, seed_end]]
        for map_ranges in maps:
            next_ranges = []
            while current_ranges:
                current_left, current_right = current_ranges.pop()
                next_ranges += are_ranges_overlapped(current_left, current_right, map_ranges)
            current_ranges = next_ranges
        if not current_ranges:
            continue
        min_location = min(min_location, min(_range[0] for _range in current_ranges))
    return min_location


if __name__ == '__main__':
    lines = open('/Users/dallenmn/PycharmProjects/adventOfCode2023/inputs/day5.txt').read().split('\n\n')

    # ranges: [inclusive, exclusive)
    seeds = parse_seeds([int(s) for s in lines[0].split()[1:]])
    mappings = parse_mappings(lines[1:])

    answer = solve_part_two(seeds, mappings)
    print(answer)
