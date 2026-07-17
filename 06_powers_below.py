"""
第6题：while 循环与幂运算
知识点：while 循环、比较运算符、幂运算符（**）、循环控制变量
"""

def powers_below(num):  # 定义函数，参数 num 表示上限值
    exponent = 0        # 初始化指数，从 0 开始（2^0 = 1）
    # while 循环：只要 2 的 exponent 次方不超过 num，就继续执行
    while 2 ** exponent <= num:  # ** 是 Python 的幂运算符，计算 2 的 exponent 次方
        print(f'2^{exponent}={2 ** exponent}')  # 打印当前结果，如 2^3=8
        exponent += 1  # 指数增加 1，准备计算下一次幂（相当于循环控制变量）

# 调用函数，打印所有不超过 100 的 2 的幂
powers_below(100)


"""
补充说明

1. while 循环的执行逻辑：
   每次循环开始前都会判断条件（2 ** exponent <= num），
   条件为 True 则执行循环体，为 False 则跳出循环。

2. 循环控制变量：
   exponent 在循环体内不断自增（exponent += 1），
   确保循环能最终终止，避免死循环。

3. 幂运算符 **：
   a ** b 表示 a 的 b 次方，本例中 2 ** exponent 即 2 的 exponent 次幂。

4. 当 num = 100 时的输出结果：
   2^0=1，2^1=2，2^2=4，2^3=8，2^4=16，2^5=32，2^6=64
   当 exponent = 7 时，2^7 = 128 > 100，循环终止。

5. 扩展思考：如果将 num 改为 0，循环还会执行吗？
   （提示：2^0 = 1，判断 1 <= 0 为 False，循环体一次都不执行）
"""