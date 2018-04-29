# http://www.pythonchallenge.com/pc/def/map.html
import os


def solve_challenge():
    input_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb." + \
        " rfyrq ufyr amknsrcpq ypc dmp." + \
        " bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." + \
        " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    a_to_z = "".join([chr(n) for n in range(ord('a'), ord('z')+1)]).encode()
    c_to_b = b"cdefghijklmnopqrstuvwxyzab"
    table = bytes.maketrans(a_to_z, c_to_b)
    print(input_text.translate(table))
    return os.path.join("http://www.pythonchallenge.com/pc/def/", "map".translate(table)) + ".html"


if __name__ == '__main__':
    print(solve_challenge())


