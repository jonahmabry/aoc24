from ..utils import parse_data


def solve_part1(data: str):
    input_data = parse_data(data)

    list1, list2 = [], []
    for line in input_data:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

    list1 = sorted(list1)
    list2 = sorted(list2)

    distance = 0
    for i in range(len(list1)):
        distance += abs(int(list1[i]) - int(list2[i]))

    return distance


def solve_part2(data: str):
    input_data = parse_data(data)

    list1, list2 = [], []
    for line in input_data:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

    similarity_score = 0
    for item in list1:
        similarity_score += list2.count(item) * item

    return similarity_score
