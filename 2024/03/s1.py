import re

if __name__ == '__main__':
    mul_input = ''
    with open('input.txt', 'r', encoding='utf-8-sig') as f:
        mul_input = f.read()

    pattern = r"mul\(\d+,\d+\)"
    patternMul = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, mul_input)

    sum = 0
    for match in matches:
        m = re.match(patternMul, match)
        n1 = int(m.group(1))
        n2 = int(m.group(2))
        sum += n1 * n2

    print(sum)