from ..utils import parse_data


def solve_part1(data: str):
    input_data = parse_data(data)
    print(input_data)

    count = 0
    lines = data.splitlines()
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                word = ""
                for i in range(4):
                    nr, nc = r + dr*i, c + dc*i
                    if 0 <= nr < rows and 0 <= nc < cols:
                        word += grid[nr][nc]
                    else:
                        break
                if word == "XMAS":
                    count += 1
    return count


def solve_part2(data: str):
    """Check if 3 consecutive letters in a certain direction is MAS"""
    input_data = parse_data(data)
    print(input_data)

    count = 0
    lines = data.splitlines()
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "A" and (0 < r < rows - 1 and 0 < c < cols - 1):
                tl_to_br = (grid[r-1][c-1] + "A" + grid[r+1][c+1])
                tr_to_bl = (grid[r-1][c+1] + "A" + grid[r+1][c-1])
                if (tl_to_br == "MAS" or tl_to_br == "SAM") and (tr_to_bl == "MAS" or tr_to_bl == "SAM"):
                    count += 1
    return count
