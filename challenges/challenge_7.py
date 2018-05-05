# http://www.pythonchallenge.com/pc/def/oxygen.html
from PIL import Image
import re


def solve_challenge():
    image = Image.open('data/oxygen.png').convert('RGB')

    # find the mid row - the greyscale line
    mid_row = [image.getpixel((x, image.height / 2)) for x in range(image.width)]

    #  each pixel is repeated 7 times so we can get every seventh pixel
    mid_row = mid_row[::7]

    #  get the coloured pixels at the end of the row
    coloured_pixels = [r for r, g, b in mid_row if r == g == b]

    # R,G,B values are represented between 0 and 255 so they can represent ASCII values
    characters = "".join(map(chr, coloured_pixels))
    print(characters)  # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

    # transform all the ASCII numbers into characters to get the name of the next level
    nums = re.findall("\d+", "".join(map(chr, coloured_pixels)))
    print("".join(map(chr, map(int, nums))))


if __name__ == '__main__':
    solve_challenge()

