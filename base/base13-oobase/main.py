'''
类相关

self = this
name 为类属性 在 __init__ 中指定
'''


class Cat:
    def __init__(self, name):
        print("初始化方法 %s" % name)
        self.name = name

    '''
    删除时
    '''

    def __del__(self):
        print("%s 去了" % self.name)

    def __str__(self):
        return "我是小猫：%s" % self.name


# 不需要使用 new 关键字
tom = Cat("Tom")
lazy_cat = Cat("大懒猫")

# 如果没有 __str__ 方法，将会打印内存地址
print(tom)
print(lazy_cat)

# 可在对象上添加属性
tom.age = 19
print(tom.age)
