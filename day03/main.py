import re

with open("input.txt") as f:
    INPUT = f.read()

def mul(x, y):
    return x * y

def execute(text):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    result = 0
    matches = re.findall(pattern, text)
    for m in matches:
        result += eval(m)  # >:)
    return result

def part1(_input):
    return execute(_input)

def part2(_input):
    result = 0
    for chunk in _input.split("do()"):
        result += execute(chunk.split("don't()")[0])
    return result

if __name__ == "__main__":
    print(part1(INPUT))
    print(part2(INPUT))
