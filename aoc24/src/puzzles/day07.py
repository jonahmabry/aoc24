import itertools

from ..utils import parse_data


def solve_part1(data: str):
    input_data = parse_data(data)
    print(input_data)

    total = 0
    for item in input_data:
        answer, nums = item.split(": ")
        answer = int(answer)
        nums = list(map(int, nums.split(" ")))
        print(answer, nums)

        for ops in itertools.product(["*","+", "||"], repeat=len(nums) - 1):
            value = nums[0]
            for op in zip(ops, nums[1:]):
                if op[0] == "*":
                    value *= op[1]
                else:
                    value += op[1]

            if value == answer:
                total += value
                break

    return total


def solve_part2(data: str):
    input_data = parse_data(data)
    print(input_data)

    total = 0
    for item in input_data:
        answer, nums = item.split(": ")
        answer = int(answer)
        nums = list(map(int, nums.split(" ")))

        for ops in itertools.product(["*","+", "||"], repeat=len(nums) - 1):
            value = nums[0]
            for op in zip(ops, nums[1:]):
                if op[0] == "*":
                    value *= op[1]
                elif op[0] == "+":
                    value += op[1]
                else:
                    value = int(str(value) + str(op[1]))

            if value == answer:
                total += value
                break

    return total
