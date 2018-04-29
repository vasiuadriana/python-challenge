# http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib.request, urllib.parse


def solve_challenge():
    input_data = {'nothing': 12345}

    for _i in range(400):
        params = urllib.parse.urlencode(input_data)
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?%s' % params
        with urllib.request.urlopen(url) as f:
            data = f.read().decode('utf-8')
            if 'and the next nothing is' in data:
                input_data['nothing'] = data.split().pop()
            elif 'Yes. Divide by two and keep going' in data:
                input_data['nothing'] = int(int(url.split('nothing=')[1]) / 2)
                print('Nothing divided: %s' % input_data['nothing'])
            else:
                return data, url


if __name__ == '__main__':
    print(solve_challenge())
