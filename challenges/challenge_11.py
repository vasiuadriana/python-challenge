# http://www.pythonchallenge.com/pc/return/5808.html
from PIL import Image


def solve_challenge():
    image = Image.open('data/cave.jpg')
    (w, h) = image.size

    even = Image.new('RGB', (w // 2, h // 2))
    odd = Image.new('RGB', (w // 2, h // 2))

    for i in range(w):
        for j in range(h):
            p = image.getpixel((i, j))
            if (i + j) % 2 == 1:
                odd.putpixel((i // 2, j // 2), p)
            else:
                even.putpixel((i // 2, j // 2), p)
    even.save('data/even.jpg')
    odd.save('data/odd.jpg')


if __name__ == '__main__':
    solve_challenge()