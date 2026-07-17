"""
第5题：累加求和（for 循环 + range 函数）
知识点：range() 生成数字序列、for 循环遍历、累加器变量、return 返回值
"""

def accumulation(num):  # 定义函数，参数 num 表示累加的终止值
    total = 0  # 初始化累加器，用于存储累加结果
    # range(1, num + 1) 生成从 1 到 num 的整数序列（左闭右开，终点不包含）
    for i in range(1, num + 1):
        total += i  # 等价于 total = total + i，将 i 累加到 total 中
    return total  # 将累加结果返回给调用者

# 调用函数，将 10 作为实参传入，返回值直接嵌入 f-string 中打印
num = 10
print(f'1到{num}的和为{accumulation(num)}')


"""
补充说明

1. range() 函数的用法：
   - range(start, stop) 生成从 start 到 stop-1 的整数序列。
   - range(1, 11) 生成 1, 2, 3, ..., 10。
   - 如果不写 start，默认从 0 开始，如 range(5) 生成 0, 1, 2, 3, 4。

2. 累加器模式：
   - 先初始化一个变量（通常为 0），然后在循环中不断累加。
   - total += i 是 total = total + i 的简写形式。

3. return 语句：
   - 将函数执行结果返回给调用者。
   - 函数执行到 return 时会立即结束，后面的代码不再执行。

4. 数学小知识：
   1 到 n 的和也可以用公式 n * (n + 1) // 2 直接计算，
   但本例使用循环是为了演示循环结构。
"""