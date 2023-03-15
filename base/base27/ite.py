"""
迭代方式 定义自定义的类
"""


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

"""
生成器1
"""
# 创建一个列表
L = [x * 2 for x in range(5)]
print(L)
print("----------这是一个分割线")

# 创建一个生成器
G = (x * 2 for x in range(5))
print(G)
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))

"""
生成器2
"""


def creatNum():
    print("---------start-----------")
    a, b = 0, 1
    for i in range(5):
        print("----1----")
        yield b
        print("----2----")
        a, b = b, a + b
        print("----3----")
    print("---------stop-----------")


a = creatNum()
print(a)
print(next(a))
print("----------这是一个分割线-----------")
print(next(a))
# 使用for
for num in a:
    print(num)


# 拿到返回值
def creatNum():
    print("---------start-----------")
    a, b = 0, 1
    for i in range(5):
        yield b
        a, b = b, a + b
    print("---------stop-----------")


a = creatNum()

while True:
    try:
        x = next(a)
        print("value:%d" % x)
    except StopIteration as e:
        print("生成器返回值:%s" % e.value)
        break


# 读取大文件
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'r', encoding='utf-8') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return


a = read_file('E:/TM_DATA_1760/TM_DATA_1760/TM_DATA_1760.json')
print(next(a))
print(next(a))
print(next(a))
