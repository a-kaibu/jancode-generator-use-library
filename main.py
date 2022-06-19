import os

import barcode
from barcode.writer import ImageWriter


def check_dir():
    if not os.path.exists("./img"):
        os.mkdir("./img")


def read_number() -> str:
    input_number: str = input("JANコードを入力してください : ")
    # もし入力が数字でなければ再入力
    if not input_number.isdigit():
        print("数字を入力してください")
        read_number()

    return input_number


def main():
    check_dir()

    input_number: str = read_number()

    jan: type = barcode.get_barcode_class("jan")
    code = jan(input_number, writer=ImageWriter())
    code.save("img/{}".format(input_number))


if __name__ == "__main__":
    main()
