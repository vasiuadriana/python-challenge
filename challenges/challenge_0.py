# URL: http://www.pythonchallenge.com/pc/def/0.html

import os
from math import pow


def solve_challenge():
    url_number = str(int(pow(2, 38)))
    return os.path.join('http://www.pythonchallenge.com/pc/def', url_number) + '.html'


if __name__ == '__main__':
    print(solve_challenge())
