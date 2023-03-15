# 列表推导
# 需求1：求列表中元素+1后的值
list_1 = [x + 1 for x in range(1, 10)]
print(list_1)  # [2, 3, 4, 5, 6, 7, 8, 9, 10]

# 需求2：求列表中元素乘10后的值
list_2 = [x * 10 for x in range(1, 10)]
print(list_2)  # [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 需求3：求列表中元素的平方
list_3 = [x * x for x in range(1, 10)]
print(list_3)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 需求1：求列表中偶数元素乘10后的值
list_2 = [x * 10 for x in range(1, 10) if x % 2 == 0]
print(list_2)  # [20, 40, 60, 80]

# 需求2：求列表中偶数元素的平方
list_3 = [x * x for x in range(1, 10) if x % 2 == 0]
print(list_3)  # [4, 16, 36, 64]

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [x for y in list1 for x in y if x % 2 == 0]
print(list2)  # [2, 4, 6, 8]

list2 = [x + y for x in 'python' for y in '12']
print(list2)  # ['p1', 'p2', 'y1', 'y2', 't1', 't2', 'h1', 'h2', 'o1', 'o2', 'n1', 'n2']

# 元组推导
tup1 = (x for x in range(0, 9))
print(tup1)  # <generator object <genexpr> at 0x000002776CFC45F0>
tup2 = tuple(x for x in range(0, 9))
print(tup2)  # (0, 1, 2, 3, 4, 5, 6, 7, 8)

list1 = ['hello', 'python', 'lalala']
dic1 = {key: len(key) for key in list1}
print(dic1)  # {'hello': 5, 'python': 6, 'lalala': 6}
# 字典推导


# 集合推导
set1 = {x for x in 'aaabcdefg123456'}
print(set1)  # {'b', '3', 'g', '2', '1', 'e', 'd', 'c', 'f', 'a', '4', '5', '6'}
