with open("input.txt") as f:
    INPUT = f.readlines()

def get(lines, x, y):
    return lines[y][x] if 0 <= x < len(lines[0]) and 0 <= y < len(lines) else None

def part1(lines):
    result = 0
    pattern = "XMAS"
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == pattern[0]:
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    n = 0
                    x2, y2 = x, y
                    while get(lines, x2, y2) == pattern[n] and not (0 > y2 > len(lines) - 1 or 0 > x2 > len(lines[0]) - 1):
                        n += 1
                        if n == len(pattern):
                            result += 1
                            break
                        x2 += d[0]
                        y2 += d[1]
    return result

def part2(lines):
    result = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "A":
                if ((get(lines, x - 1, y - 1) == "M" and get(lines, x + 1, y + 1) == "S") or (     # ↘ 
                     get(lines, x - 1, y - 1) == "S" and get(lines, x + 1, y + 1) == "M")) and ((  # ↖
                     get(lines, x - 1, y + 1) == "M" and get(lines, x + 1, y - 1) == "S") or (     # ↗
                     get(lines, x - 1, y + 1) == "S" and get(lines, x + 1, y - 1) == "M")):        # ↙
                    result += 1
    return result

if __name__ == "__main__":
    print(part1(INPUT))
    print(part2(INPUT))
