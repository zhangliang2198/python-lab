import random

print("没有设定种子时")
for i in range(5):
    ret = random.randint(1, 10)
    print(ret, end=" ")
print()

print("设定种子时")
random.seed(1)
for i in range(5):
    ret = random.randint(1, 10)
    print(ret, end=" ")

"""
随机密码字符集
"""
import random
import string


def get_random_string(length):
    # 随机生成字母和数字的位数
    num_count = random.randint(1, length - 1)
    letter_count = length - num_count

    # 随机抽样生成数字序列
    num_list = [random.choice(string.digits) for _ in range(num_count)]

    # 随机抽样生成字母序列
    letter_list = [random.choice(string.ascii_letters) for _ in range(letter_count)]

    # 合并字母和数字
    all_list = num_list + letter_list

    # 乱序
    random.shuffle(all_list)

    result = "".join([i for i in all_list])
    return result


print()
# 生成10位的密码
password1 = get_random_string(10)
print(password1)
# 生成15位的密码
password2 = get_random_string(15)
print(password2)
# 生成20位的密码
password3 = get_random_string(20)
print(password3)

"""
圆周率的奇怪算法
"""
DARTS = 1000 * 1000 * 10
hits = 0.0

for i in range(1, DARTS + 1):
    x, y = random.random(), random.random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits / DARTS)
print("圆周率值是：%s" % pi)
