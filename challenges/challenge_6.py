# http://www.pythonchallenge.com/pc/def/channel.html
import zipfile


def solve_challenge():
    with zipfile.ZipFile('data/channel.zip') as zip_file:
        file_name = '90052'
        comments = []
        while True:
            comments.append(zip_file.getinfo('%s.txt' % file_name).comment.decode('utf-8'))
            with zip_file.open('%s.txt' % file_name) as f:

                data = f.read().decode('utf-8')
                if 'Next nothing is' in data:
                    file_name = data.split()[-1]
                else:
                    print(data)  # Collect the comments
                    break
    return ''.join(comments)  # hockey


if __name__ == '__main__':
    print(solve_challenge())