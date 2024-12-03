import re

if __name__ == '__main__':
    mul_input = ''
    with open('input.txt', 'r', encoding='utf-8-sig') as f:
        mul_input = f.read()

    pattern = r"mul\(\d+,\d+\)|don'?t\(\)|do\(\)"
    patternMul = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, mul_input)

    sum = 0
    mul_enabled = True
    for match in matches:
        if match == "do()":
            mul_enabled = True
        elif match == "don't()":
            mul_enabled = False
        else:
            if not mul_enabled:
                continue
            m = re.match(patternMul, match)
            n1 = int(m.group(1))
            n2 = int(m.group(2))
            sum += n1 * n2

    print(sum)