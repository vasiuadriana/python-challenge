# http://www.pythonchallenge.com/pc/return/bull.html
import re


def solve_challenge():
    # a = [1, 11, 21, 1211, 111221, ... is a look and say sequence
    # to generate a member of the sequence from the previous member, read off the digits of the previous member,
    # counting the number of digits in groups of the same digit. For example:
    # 1 is read off as "one 1" or 11.
    # 11 is read off as "two 1s" or 21.
    # 21 is read off as "one 2, then one 1" or 1211.
    # 1211 is read off as "one 1, one 2, then two 1s" or 111221.
    # 111221 is read off as "three 1s, two 2s, then one 1" or 312211.
    pattern = r"(\d)(\1*)"
    print(re.findall(pattern, '1'))  # outputs [('1', '')]
    print(re.findall(pattern, '11'))  # outputs [('1', '1')]
    print(re.findall(pattern, '21'))  # outputs [('2', ''), ('1', '')]
    print(re.findall(pattern, '1211'))  # outputs [('1', ''), ('2', ''), ('1', '1')]
    print(re.findall(pattern, '111221'))  # outputs [('1', '11'), ('2', '2'), ('1', '')]

    x = '1'
    for n in range(30):
        x = "".join([str(len(j) + 1) + i for i, j in re.findall(pattern, x)])
    return len(x)


if __name__ == '__main__':
    print(solve_challenge())
