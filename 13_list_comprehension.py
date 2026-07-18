"""
第13题：列表推导式
知识点：列表推导式的基本语法、条件筛选、对原列表元素进行运算处理
"""

def demonstrate_list_comprehension():  # 函数名清晰表达"演示列表推导式"的功能
    # ---------- 基础用法：生成数字序列 ----------
    # 列表推导式 [x for x in range(1, 11)] 等价于：
    # for x in range(1, 11): 每次取出 x，直接放入新列表
    numbers = [x for x in range(1, 11)]  # 生成 1 到 10 的整数列表
    print(f"1到10的数字列表为：{numbers}")  # 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # ---------- 带条件筛选的列表推导式 ----------
    # 列表推导式 [x for x in numbers if x % 2 == 0] 等价于：
    # for x in numbers: 如果 x % 2 == 0（偶数），则放入新列表
    even_numbers = [x for x in numbers if x % 2 == 0]  # 只取偶数
    print(f"1到10的偶数为：{even_numbers}")  # 输出：[2, 4, 6, 8, 10]

    # ---------- 对字符串列表进行筛选 ----------
    words = ['hello', 'welcome', 'python', 'world']  # 原始字符串列表

    # 筛选出长度大于 5 的单词
    # len(x) > 5 作为条件，只保留长度超过 5 的字符串
    long_words = [x for x in words if len(x) > 5]
    print(f"长度大于5的单词为：{long_words}")  # 输出：['welcome', 'python']

# 调用函数执行演示
demonstrate_list_comprehension()


"""
补充说明

1. 列表推导式的基本语法：
   [新元素 for 变量 in 可迭代对象]

   依次遍历可迭代对象中的每个元素，对每个元素执行表达式，将结果放入新列表。

2. 带条件的列表推导式：
   [新元素 for 变量 in 可迭代对象 if 条件]

   只有满足条件的元素才会被处理并放入新列表，相当于在循环内部加了 if 判断。

3. 列表推导式 vs 普通 for 循环：
   - 列表推导式更简洁，代码量更少。
   - 普通 for 循环可读性更强（尤其是复杂逻辑时）。
   - 两者性能差异不大，初学者可先掌握 for 循环再学推导式。

4. 筛选偶数的逻辑：
   x % 2 == 0 表示 x 除以 2 的余数为 0，即偶数。
   x % 2 == 1 或 x % 2 != 0 表示奇数。

5. len() 函数：
   len(字符串) 返回字符串的字符个数（中英文均按 1 个字符计算）。
   len('hello') = 5，len('welcome') = 7，len('python') = 6，len('world') = 5。

6. 命名优化说明：
   - 原函数名 lb 改为 demonstrate_list_comprehension，清晰表达功能。
   - arr1 改为 numbers，表达"数字列表"。
   - arr2 改为 even_numbers，表达"偶数列表"。
   - arr3 改为 words，表达"单词列表"。
   - arr4 改为 long_words，表达"长单词列表"。
   - 使用描述性命名让代码自解释，无需额外注释即可理解。

7. 扩展思考：
   - 如何生成 1 到 10 的平方列表？[x**2 for x in range(1, 11)]
   - 如何筛选出长度小于等于 5 的单词？修改条件为 len(x) <= 5
   - 列表推导式是否可以嵌套使用？可以，如 [y for x in matrix for y in x]
   - 除了列表，还有字典推导式、集合推导式，语法类似。
"""