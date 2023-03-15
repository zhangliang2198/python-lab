# def函数写法
# 定义加法函数
def add(a, b):
    return a + b


print(add(10, 20))
print("----------这是一个分割线----------")

# lambda函数写法
add_lambda = lambda a, b: a + b
print(add_lambda(10, 20))


# 使用if判断奇偶性
# def函数写法
def get_odd_even(x):
    if x % 2 == 0:
        return "偶数"
    else:
        return "奇数"


print(get_odd_even(10))
print("----------这是一个分割线----------")

# lambda函数写法
get_odd_even1 = lambda x: "偶数" if x % 2 == 0 else "奇数"
print(get_odd_even1(10))
print(get_odd_even1(9))


# 和map一起
# def函数写法
def add(num):
    return num ** 2


x = map(add, [1, 2, 3, 4, 5])
print(list(x))
print("----------这是一个分割线----------")

# lambda函数写法
y = map(lambda num: num ** 2, [1, 2, 3, 4, 5])
print(list(y))

# filter
x = filter(lambda num: num % 2 == 0, range(10))
print(list(x))

# reduce
from functools import reduce

list1 = [1, 2, 3, 4, 5]
list2 = reduce(lambda x, y: x + y, list1)
print(list2)  # 15
