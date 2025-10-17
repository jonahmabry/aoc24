import random

from ..utils import parse_data


def solve_part1(data: str):
    input_data = parse_data(data)
    print(input_data)

    updates = []
    rules = []
    count = 0

    for ix, item in enumerate(input_data):
        if item == "":
            updates = input_data[ix+1:]
            rules = input_data[:ix]

    for update in updates: # For every update in the list of updates
        passed = True
        new_updates = list(map(int, update.split(","))) # Turn each update into a list of integers
        for rule in rules: # For every rule in the list of rules
            num1 = int(rule.split("|")[0])
            num2 = int(rule.split("|")[1]) # Set the first number to num1 and the second number to num2
            if num1 in new_updates and num2 in new_updates: # If both num1 and num2 are in new_updates
                if new_updates.index(num1) < new_updates.index(num2) and passed: # If the element at num1 comes before the element at num2
                    # print(f"Passed at {update} in {new_updates} bc of rule {rule}")
                    passed = True #
                else:
                    # print(f"Broken at {update} in {new_updates} bc of rule {rule}")
                    passed = False
                    break
        if passed:
            count += new_updates[len(new_updates) // 2]
            # print(f"Middle of {new_updates} is {new_updates[len(new_updates) // 2]}")

    return count


def check_rule(rules, new_updates):
    for a, b in rules:  # For every rule in the list of rules
        if a in new_updates and b in new_updates:  # If both num1 and num2 are in new_updates
            if new_updates.index(a) > new_updates.index(b):  # If the element at num1 comes after the element at num2
                return False
    return True

def solve_part2(data: str):
    input_data = parse_data(data)

    split_index = input_data.index("")
    rules = input_data[:split_index]
    updates = input_data[split_index+1:]

    rule_pairs = [(int(a), int(b)) for a, b in (r.split("|") for r in rules)]
    count = 0

    for update in updates: # For every update in the list of updates
        new_updates = list(map(int, update.split(",")))  # Turn each update into a list of integers
        passed = check_rule(rule_pairs, new_updates)

        if passed:
            continue

        while not passed:
            for a, b in rule_pairs:
                if a in new_updates and b in new_updates:
                    i, j = new_updates.index(a), new_updates.index(b)
                    if i > j:
                        new_updates[i], new_updates[j] = new_updates[j], new_updates[i]
                        passed = check_rule(rule_pairs, new_updates)

        count += new_updates[len(new_updates) // 2]

    return count
