# http://www.pythonchallenge.com/pc/def/ocr.html


def solve_challenge():
    char_frequency = {}
    file_path = 'data/data_challenge_two.txt'
    with open(file_path) as f:
        data = ''.join(f.read().splitlines())
        for c in data:
            try:
                char_frequency[c] += 1
            except KeyError:
                char_frequency[c] = 1
    return "".join([k for k, v in char_frequency.items() if v == 1])


if __name__ == '__main__':
    print(solve_challenge())