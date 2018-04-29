# http://www.pythonchallenge.com/pc/def/equality.html
import re


def solve_challenge():
    file_path = 'data/data_challenge_three.txt'
    with open(file_path) as f:
        data = ''.join(f.read().splitlines())
        pattern = re.compile('([a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z])')
        matches = pattern.findall(data)
        return ''.join([match[1] for match in matches])


if __name__ == '__main__':
    print(solve_challenge())