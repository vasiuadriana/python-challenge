# http://www.pythonchallenge.com/pc/def/peak.html
import urllib.request
import pickle


def solve_challenge():
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    with urllib.request.urlopen(url) as f:
        pickled_obj = pickle.load(f)
        for el in pickled_obj:
            output = ''.join([e[0] * e[1] for e in el])
            print(output)


if __name__ == '__main__':
    solve_challenge()
