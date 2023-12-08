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

        # sorting doesn't matter, but makes debugging easier
        parsed_rules.sort(key=lambda x: x[0])
        parsed_rules.append([parsed_rules[-1][1], float('inf'), 0])
        if parsed_rules[0][0] != 0:
            parsed_rules.append([0, parsed_rules[0][0], 0])
        parsed_rules.sort(key=lambda x: x[0])

        """
        I think I got lucky here that there were no "in-between" ranges that would default to the 0 offset case.
        Since this works with the solution case, I'm not going to spend more time adding it here. Just noting it.
        """

        parsed_maps.append(parsed_rules)
    return parsed_maps


def are_ranges_overlapped(left, right, range_start, range_end):
    # 4 overlapping cases:
    #   case1           case2           case3           case4
    #  |----|       |-----|             |------|     |--------|
    # |------|        |------|        |------|        |------|
    case1 = left >= range_start and right <= range_end
    case2 = left <= range_start < right <= range_end
    case3 = range_start <= left < range_end <= right
    case4 = left <= range_start and right >= range_end
    return case1 or case2 or case3 or case4


def generate_next_ranges(left, right, map_ranges):
    next_ranges = []
    for range_start, range_end, offset in map_ranges:
        if are_ranges_overlapped(left, right, range_start, range_end):
            next_range_start = max(range_start, left) + offset
            next_range_end = min(range_end, right) + offset
            next_ranges.append([next_range_start, next_range_end])
    return next_ranges


def solve_part_two(seed_ranges, maps):
    """
    for each seed range:
        for each mapping:
            1. filter out the current map ranges that don't overlap
            2. add the offset to the ranges that do overlap
        record the smallest location found from this seed range
    return the smallest location found from all the seed ranges
    """
    min_location = float('inf')
    for seed_start, seed_end in seed_ranges:
        current_ranges = [[seed_start, seed_end]]
        for map_ranges in maps:
            next_ranges = []
            while current_ranges:
                current_left, current_right = current_ranges.pop()
                next_ranges += generate_next_ranges(current_left, current_right, map_ranges)
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
