# if 条件语句
# number = int(input("请输入你的成绩: "))
number = 60
if number >= 90:
    print("优秀")
elif number >= 80:
    print("良好")
elif number >= 70:
    print("不错")
elif number >= 60:
    print("及格")
else:
    print("不及格")

# 嵌套 if
# num = int(input("输入一个数字："))
num = 15
if num > 0:
    if num >= 18:
        print("已成年")
    else:
        print("未成年")
else:
    print("刚出生")

# while语句
# 1.编写循环 确定 要计算的数字
# 2. 添加 结果  变量，在循环内部 处理计算结果
i = 0
while i <= 100:
    print(i, end=" ")
    i += 1

print()
# 最终代码如下
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# while…else
age = 0
while age < 3:
    print(age, "年龄小于3")
    age = age + 1
else:
    print(age, "年龄大于等于3")

# while 嵌套 9 9 乘法表
# 定义起始行
row = 1
# 最大打印 9 行
while row <= 9:
    # 定义起始列
    col = 1
    # 最大打印 row 列
    while col <= row:
        # end = ""，表示输出结束后，不换行
        # "\t" 可以在控制台输出一个制表符，协助在输出文本时对齐
        print("%d * %d = %d" % (col, row, row * col), end="\t")
        # 列数 + 1
        col += 1
    # 这行代码的目的是一行输出完后之后，添加换行！
    print("")
    # 行数 + 1
    row += 1

# 循环语句（for、for…else）
# 案例1：
lists = ['小白', 20, '四川']
for i in lists:
    print(i, end=" ")
# 小白 20 四川

# 案例2：
str = 'abcd'
for i in str:
    print(i, end=" ")
# a b c d

# 案例3:
lists = ['小白', 20, '四川']
for i in lists:
    print(i)
else:
    print("遍历结束！")

# range 函数
# 案例1：
for i in range(5):
    print(i, end=" ")
# 0 1 2 3 4
print()
# 案例2（增加步长，如数字3）：
for i in range(0, 10, 3):
    print(i, end=" ")
# 0 3 6 9

print()
# break、continue
# for循环中使用break
for i in range(1, 10):
    if i % 2 == 0:
        break
    print(i, end=" ")
# 输出结果：1，因为2对2取余等于0就结束循环了
print()
# for循环中使用continue
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
# 输出结果：1 3 5 7 9 ，跳过了偶数
print()
# while循环中使用break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n, end=" ")
# 输出结果：4 3，当n=2时结束循环不输出
print()
# while循环中使用continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end=" ")
# 输出结果：4 3 1 0 ，当n=2时就跳过继续下一次循环
