"""
函数的定义和调用
"""
name = "小明"


# 解释器知道这里定义了一个函数
def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)
# 只有在调用函数时，之前定义的函数才会被执行
# 函数执行完成之后，会重新回到之前的程序中，继续执行后续的代码
say_hello()

print(name)


# 带参数和返回值的函数
def sum_2_num(num1, num2):
    """对两个数字的求和"""
    return num1 + num2


# 调用函数，并使用 result 变量接收计算结果
result = sum_2_num(10, 20)

print("计算结果是 %d" % result)
