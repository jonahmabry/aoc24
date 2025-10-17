from ..utils import parse_data


def is_safe(level):
    if level == sorted(level):
        return all(1 <= level[i] - level[i - 1] <= 3 for i in range(1, len(level)))
    if level == sorted(level, reverse=True):
        return all(1 <= level[i - 1] - level[i] <= 3 for i in range(1, len(level)))
    return False


def solve_part1(data: str):
    input_data = parse_data(data)

    count = 0
    for line in input_data:
        level = list(map(int, line.split()))

        if is_safe(level):
            count += 1
            continue
    return count


def solve_part2(data: str):
    input_data = parse_data(data)

    count = 0
    for line in input_data:
        level = list(map(int, line.split()))

        if is_safe(level):
            count += 1
            continue

        for i in range(len(level)):
            new_level = level[:i] + level[i + 1:]
            if is_safe(new_level):
                count += 1
                break
    return count
