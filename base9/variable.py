'''
變量都是引用类型
'''


def test(num):
    print("-" * 50)
    print("%d 在函数内的内存地址是 %x" % (num, id(num)))

    result = 100

    print("返回值 %d 在内存中的地址是 %x" % (result, id(result)))
    print("-" * 50)

    return result


a = 10
print("调用函数前 内存地址是 %x" % id(a))

r = test(a)

print("调用函数后 实参内存地址是 %x" % id(a))
print("调用函数后 返回值内存地址是 %x" % id(r))

'''
修改全局变量的值
'''
num = 10


def demo1():
    print("demo1" + "-" * 50)

    # global 关键字，告诉 Python 解释器 num 是一个全局变量
    global num
    # 只是定义了一个局部变量，不会修改到全局变量，只是变量名相同而已
    num = 100
    print(num)


def demo2():
    print("demo2" + "-" * 50)
    print(num)


demo1()
demo2()

print("over")
