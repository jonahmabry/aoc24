import re

from ..utils import parse_data


def solve_part1(data: str):
    input_data = str(data)
    print(input_data)

    count = sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", input_data))

    return count


def solve_part2(data: str):
    print(data)

    matches = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
    print(matches)

    count, enabled = 0, True
    for match in matches:
        print(match)
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            nums = match[4:-1].split(",")
            a, b = map(int, nums)
            count += a * b

    print(count)
    return count
