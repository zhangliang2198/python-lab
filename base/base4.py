# 字符串格式化
name = '小袁'
age = 20
# 语法一：%
print('我的名字是：%s ,年龄是：%d' % (name, age))  # 我的名字是：小袁 ,年龄是：20
# 语法二：f'{表达式}'
print(f'我的名字是：{name},我的年龄是：{age}')  # 我的名字是：小袁,我的年龄是：20

# 元组
tup1 = ('hello', 'world', 1, 2)
print(tup1)  # ('hello', 'world', 1, 2)
print(type(tup1))  # <class 'tuple'>

# 遍历元组
for i in tup1:
    print(i, end=" ")

# 修改列表
a = [1, 2, 3, 4, 5]
# 下表索引的方式修改
a[0] = 9
print(a)  # [9, 2, 3, 4, 5]

# append()方法：追加列表
a.append(6)
print(a)  # [9, 2, 3, 4, 5, 6]

# del 语句来删除列表的的元素
del a[0]
print(a)  # [2, 3, 4, 5, 6]

# 嵌套列表
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']

x = [a, b]
print(x)  # [[1, 2, 3, 4, 5], ['a', 'b', 'c']]
print(x[0])  # [1, 2, 3, 4, 5]
print(x[0][1])  # 2

# 遍历列表
a = [1, 2, 3, 4, 5]

for i in a:
    print(i, end=" ")
# 1 2 3 4 5

'''
字典
'''
# 打印字典的值
dict = {'Name': '小明', 'Age': 20}
print(dict)  # {'Name': '小明', 'Age': 20}

print(dict['Name'])  # 小明
print(dict['Age'])  # 20

# 修改字典
dict = {'Name': '小明', 'Age': 20}

dict['Name'] = '小黑'
dict['Age'] = 22

print(dict)  # {'Name': '小黑', 'Age': 22}

# 遍历字典
dict = {'Name': '小明', 'Age': 20}

# 遍历键
for key in dict.keys():
    print(key)
# 遍历值
for value in dict.values():
    print(value)

'''
集合类型
'''
# 创建方式
set1 = {'小黑', 20, 20}
print(set1)  # {'小黑', 20} ；元素不重复只显示一个20

set2 = set('abcd')
print(set2)  # {'c', 'b', 'd', 'a'} ; 元素没有顺序

# 修改集合
set1 = {'小黑', 20, 20}

# add()：添加方法
set1.add('大学生')
print(set1)  # {'大学生', '小黑', 20}

# update()：也可以添加元素，且参数可以是列表，元组，字典等
set1.update([1, 2], [3, 4])
print(set1)  # {1, '大学生', 2, 3, 4, 20, '小黑'}

# remove()：移除元素
set1.remove('大学生')
print(set1)  # {1, 2, 3, 4, 20, '小黑'}
# 遍历
set1 = {'小黑', 20, 20}

for i in set1:
    print(i, end=" ")

'''
类型装换
'''
# 定义float变量
f = 9.99
# 定义bool类型变量
b1 = False
b2 = True
# 定义str类型变量
s = '111'

# 使用int()函数
int1 = int(f)
int2 = int(b1)
int3 = int(b2)
int4 = int(s)

print("int1:", int1)
print("int1的类型是：", type(int1))
print("-" * 10)

print("int2:", int2)
print("int2的类型是：", type(int2))
print("int3:", int3)
print("int3的类型是：", type(int3))
print("-" * 10)

print("int3:", int4)
print("int3的类型是：", type(int4))

'''
boolean 类型转换
'''
# 定义int变量
i1 = 0
i2 = -1
i3 = 1
# 定义float变量
f1 = 0.0
f2 = -1.0
f3 = 1.0
# 定义str变量
s1 = ''
s2 = '0'
s3 = '-1'
s4 = '1'
s5 = 'A'

# 使用bool()函数
b1 = bool(i1)
b2 = bool(i2)
b3 = bool(i3)
b4 = bool(f1)
b5 = bool(f2)
b6 = bool(f3)
b7 = bool(s1)
b8 = bool(s2)
b9 = bool(s3)
b10 = bool(s4)
b11 = bool(s5)

print("b1:", b1)
print("b1的类型是：", type(b1))
print("b2:", b2)
print("b2的类型是：", type(b2))
print("b3:", b3)
print("b3的类型是：", type(b3))
print("-" * 10)

print("b4:", b4)
print("b4的类型是：", type(b4))
print("b5:", b5)
print("b5的类型是：", type(b5))
print("b6:", b6)
print("b6的类型是：", type(b6))
print("-" * 10)

print("b7:", b7)
print("b7的类型是：", type(b7))
print("b8:", b8)
print("b8的类型是：", type(b8))
print("b9:", b9)
print("b9的类型是：", type(b9))
print("b10:", b10)
print("b10的类型是：", type(b10))
print("b11:", b11)
print("b11的类型是：", type(b11))

'''
str() 转换
'''
# 定义int类型变量
i1 = 1
# 定义float类型变量
f1 = 9.99
# 定义bool类型变量
b1 = False
b2 = True
# 定义list类型变量
l1 = [1, 2, 'a', 'b']
# 定义tuple类型变量
t1 = (1, 2, 'a', 'b')
# 定义set类型变量
s1 = {1, 2, 'a', 'b'}
# 定义dict类型变量
d1 = {'name': '小白', 'age': 18}

# 使用str()函数
str1 = str(i1)
str2 = str(f1)
str3 = str(b1)
str4 = str(b2)
str5 = str(l1)
str6 = str(t1)
str7 = str(s1)
str8 = str(d1)

print("str1:", str1)
print("str1的类型是：", type(str1))
print("-" * 10)

print("str2:", str2)
print("str2的类型是：", type(str2))
print("-" * 10)

print("str3:", str3)
print("str3的类型是：", type(str3))
print("str4:", str4)
print("str4的类型是：", type(str4))
print("-" * 10)

print("str5:", str5)
print("str5的类型是：", type(str5))
print("-" * 10)

print("str6:", str6)
print("str6的类型是：", type(str6))
print("-" * 10)

print("str7:", str7)
print("str7的类型是：", type(str7))
print("-" * 10)

print("str8:", str8)
print("str8的类型是：", type(str8))

'''
list 类型转换
'''
# 定义tuple变量
t1 = (1, 2, 'a', 'b')
# 定义set变量
s1 = {1, 2, 'a', 'b'}
# 定义dict变量
d1 = {'name': '小白', 'age': 18}

# 使用list()函数
l1 = list(t1)
l2 = list(s1)
l3 = list(d1)

print("l1:", l1)
print("l1的类型是：", type(l1))
print("-" * 10)

print("l2:", l2)
print("l2的类型是：", type(l2))
print("-" * 10)

print("l3:", l3)
print("l3的类型是：", type(l3))

'''
truple 转换
'''
# 定义list变量
l1 = [1, 2, 'a', 'b']
# 定义set变量
s1 = {1, 2, 'a', 'b'}
# 定义dict变量
d1 = {'name': '小白', 'age': 18}

# 使用tuple()函数
t1 = tuple(l1)
t2 = tuple(s1)
t3 = tuple(d1)

print("t1:", t1)
print("l1的类型是：", type(t1))
print("-" * 10)

print("t2:", t2)
print("t2的类型是：", type(t2))
print("-" * 10)

print("t3:", t3)
print("t3的类型是：", type(t3))

'''
set() 类型转换
'''
# 定义list变量
l1 = [1, 2, 'a', 'b']
# 定义tuple变量
t1 = (1, 2, 'a', 'b')
# 定义dict变量
d1 = {'name': '小白', 'age': 18}

# 使用set()函数
s1 = set(l1)
s2 = set(t1)
s3 = set(d1)

print("s1:", s1)
print("s1的类型是：", type(s1))
print("-" * 10)

print("s2:", s2)
print("s2的类型是：", type(s2))
print("-" * 10)

print("s3:", s3)
print("s3的类型是：", type(s3))
