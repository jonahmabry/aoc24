from ..utils import parse_data


def solve_part1(data: str):
    lines = data.splitlines()
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])

    pr, pc = 0, 0
    for r in range(rows):
        print(grid[r])
        for c in range(cols):
            if grid[r][c] == '^':
                pr, pc = r, c

    """
    ^ (-1,  0) Facing up
    < ( 0, -1) Facing left
    > ( 0,  1) Facing right
    v ( 1,  0) Facing down
    """

    escaped = False

    while not escaped:
        match grid[pr][pc]:
            case '^':
                while pr > 0 and grid[pr-1][pc] != '#':
                    grid[pr-1][pc] = '^'
                    grid[pr][pc] = 'X'
                    pr -= 1
                grid[pr][pc] = '>'
                if pr == 0:
                    escaped = True
                    grid[pr][pc] = 'X'
            case '>':
                while pc < cols - 1 and grid[pr][pc+1] != '#':
                    grid[pr][pc+1] = '>'
                    grid[pr][pc] = 'X'
                    pc += 1
                grid[pr][pc] = 'v'
                if pc == cols - 1:
                    escaped = True
                    grid[pr][pc] = 'X'
            case '<':
                while pc > 0 and grid[pr][pc-1] != '#':
                    grid[pr][pc-1] = '<'
                    grid[pr][pc] = 'X'
                    pc -= 1
                grid[pr][pc] = '^'
                if pc == 0:
                    escaped = True
                    grid[pr][pc] = 'X'
            case 'v':
                while pr < rows - 1 and grid[pr+1][pc] != '#':
                    grid[pr+1][pc] = 'v'
                    grid[pr][pc] = 'X'
                    pr += 1
                grid[pr][pc] = '<'
                if pr == rows - 1:
                    escaped = True
                    grid[pr][pc] = 'X'

        # for r in range(rows):
            # print(grid[r])
        # print()

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                count += 1
    return count


def simulate(grid, start, start_dir=0):
    rows, cols = len(grid), len(grid[0])
    r, c = start
    direction = start_dir
    visited = set()

    while True:
        if (r,c, direction) in visited:
            return True # loop detected
        visited.add((r,c, direction))

        dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            return False

        # Turn right on obstacle
        if grid[nr][nc] == '#':
            direction = (direction + 1) % 4
        else:
            r, c = nr, nc


def solve_part2(data: str):
    start = None
    lines = data.splitlines()
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '^':
                start = r, c

    loops = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r, c) != start:
                grid[r][c] = '#'
                if simulate(grid, start):
                    loops += 1
                grid[r][c] = '.' # reset

    return loops