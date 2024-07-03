def outer_function():
    try:
        inner_function()
    except StopOuterFunction:
        print("Stopping outer_function")


def inner_function():
    # 在这里抛出异常以停止外层函数
    raise StopOuterFunction


class StopOuterFunction(Exception):
    pass


# 调用外层函数
outer_function()

print('Hello world')
