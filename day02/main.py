with open("input.txt") as f:
    INPUT = f.readlines()

def parse(lines):
    return [list(map(int, l.split())) for l in lines]

def check1(line):
    if line == sorted(line) or line == sorted(line, reverse=True):
        return True
    return False

def check2(line):
    for i in range(1, len(line)):
        change = abs(line[i] - line[i-1]) 
        if change < 1 or change > 3:
            return False
    return True

def part1(parsed_input):
    result = 0
    for line in parsed_input:
        if check1(line) and check2(line):
            result += 1
    return result

def part2(parsed_input):
    result = 0
    for line in parsed_input:
        if check1(line) and check2(line):
            result += 1
        else:
            for i in range(len(line)):
                damped = line.copy()
                damped.pop(i)
                if check1(damped) and check2(damped):
                    result += 1
                    break
    return result

if __name__ == "__main__":
    print(part1(parse(INPUT)))
    print(part2(parse(INPUT)))

