from utils import *
from bili import bilibili
from nem import neteasemusic


def main():
    while True:
        user_input: str = input(">> ")

        if user_input == "quit":
            break

        # 检查url类型
        url_type: str = check(user_input)

        # 调用与url_type同名的函数
        if url_type:
            globals()[url_type.lower()](user_input)
        else:
            error("Sorry, this url is not supported.")


if __name__ == "__main__":
    logo()
    hint()
    main()
