"""
基础装饰
"""


def w1(func):
    """装饰器函数"""

    def inner():
        func()
        print("这是添加的新功能")

    return inner


@w1  # 等同于调用函数的时候上方加上：f1 = w1(f1)
def f1():
    """业务函数"""
    print("---f1---")


@w1
def f2():
    """业务器函数"""
    print("---f2---")


f1()
f2()

"""
多个装饰器
"""


def w1(fn):
    """装饰器函数"""

    def inner():
        print("---1---")
        return "<b>" + fn() + "</b>"

    return inner


def w2(fn):
    """装饰器函数"""

    def inner():
        print("---2---")
        return "<i>" + fn() + "</i>"

    return inner


@w1
@w2
def f1():
    """业务函数"""
    print("---3---")
    return "hello python"


ret = f1()
print(ret)

"""
传参
"""


def w1(fn):
    """装饰器函数"""
    print("---正在装饰---")

    def inner(a, b):  # 如果a, b没有定义，那么会导致19行代码调用失败
        print("---正在验证---")
        fn(a, b)  # 如果没有把a, b当实参进行传递，那么会导致调用13行的函数失败

    return inner


@w1
def f1(a, b):
    """业务函数"""
    print(a + b)


f1(10, 20)

"""
不定长
"""


def w1(fn):
    """装饰器函数"""
    print("---正在装饰---")

    def inner(*args, **kwargs):  # 如果a, b没有定义，那么会导致19行代码调用失败
        print("---正在验证---")
        fn(*args, **kwargs)  # 如果没有把a, b当实参进行传递，那么会导致调用13行的函数失败

    return inner


@w1
def f1(a, b):
    """业务函数"""
    print(a + b)


@w1
def f2(a, b, c):
    """业务函数"""
    print(a + b + c)


f1(10, 20)
f2(10, 20, 30)

"""
装饰器返回值
"""


def w1(fn):
    """装饰器函数"""
    print("---正在装饰---")

    def inner():
        print("---正在验证---")
        ret = fn()  # 保存返回来的字符串
        return ret  # 把字符串返回到20行的调用处

    return inner


@w1
def test():
    """业务函数"""
    print("---test---")
    return "这是原函数返回值"


ret = test()  # 需要用参数来接收返回值
print(ret)

"""
通用装饰器
"""


def w1(fn):
    """装饰器函数"""

    def inner(*args, **kwargs):
        print("---记录日志---")
        ret = fn(*args, **kwargs)  # 保存返回来的字符串
        return ret  # 把字符串返回到20行的调用处

    return inner


@w1
def test1():
    """不带返回值"""
    print("---test1---")


@w1
def test2():
    """带返回值"""
    print("---test2---")
    return "这是原函数返回值"


@w1
def test3(a):
    """业务函数"""
    print("---test3中的数据:%d---" % a)


ret1 = test1()
print(ret1)
ret2 = test2()
print(ret2)
ret3 = test3(10)
print(ret3)

"""
装饰器带参数
"""


def func_arg(arg):
    def func(funtionName):
        def func_in():
            print("输出给装饰器传入的参数:%s" % arg)
            if arg == "hello":
                funtionName()
                funtionName()
            else:
                funtionName()

        return func_in

    return func


@func_arg("hello")
def test():
    print("---test---")


@func_arg("haha")
def test2():
    print("---test2---")


test()
test2()
