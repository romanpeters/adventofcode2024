with open("input.txt") as f:
    INPUT = f.readlines()

def parse(lines) -> ([], []):
    left, right = [], []
    for line in lines:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[-1]))
    return (left, right)

def part1(lines):
    left, right = parse(lines)
    result = 0
    left.sort()
    right.sort()

    for i in range(len(left)):
        result += abs(left[i] - right[i])
    return result

def part2(lines):
    left, right = parse(lines)
    result = 0
    for n in left:
        result += n * right.count(n)
    return result
        

if __name__=="__main__":
    print(part1(INPUT))
    print(part2(INPUT))
