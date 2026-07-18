"""
第11题：异常处理（try / except）
知识点：try-except 捕获异常、ZeroDivisionError 除零错误、
       TypeError 类型错误、异常处理的代码保护机制
"""

def divide_numbers(dividend, divisor):  # 函数名清晰表达"做除法运算"的功能
    """安全的除法函数，捕获并处理可能的异常"""
    try:  # 尝试执行可能出错的代码
        result = dividend / divisor  # 执行除法运算
        return result  # 如果没有异常，返回计算结果
    except ZeroDivisionError:  # 捕获除数为零的错误
        return "错误：除数不能为零！"
    except TypeError:  # 捕获类型错误（如数字与字符串相除）
        return "错误：输入类型不正确，请输入数字！"

# 准备测试数据：包含正常、除零、类型错误三种情况
test_cases = [
    (10, 2),      # 正常情况：10 / 2 = 5
    (5, 0),       # 异常情况：除数为零，触发 ZeroDivisionError
    (3, 'a')      # 异常情况：字符串与数字相除，触发 TypeError
]

# 遍历测试数据，调用函数并打印结果
for dividend, divisor in test_cases:
    result = divide_numbers(dividend, divisor)  # 调用安全除法函数
    print(f"{dividend}/{divisor} = {result}")   # 打印运算表达式和结果


"""
补充说明

1. 异常处理的基本结构：
   try：
       可能出错的代码
   except 异常类型：
       捕获到特定异常时执行的代码

   当 try 中的代码发生异常时，程序不会崩溃，而是跳转到对应的 except 分支执行。

2. 本例涉及的两种异常：
   - ZeroDivisionError：当除数为 0 时触发（数学上不允许除以零）。
   - TypeError：当操作数类型不匹配时触发，如数字除以字符串。

3. except 的匹配规则：
   - 程序从上到下依次匹配 except 分支。
   - 一旦匹配到对应的异常类型，执行该分支的代码，然后跳过其他 except。
   - 如果异常没有匹配到任何 except，程序仍会崩溃（本例中已覆盖所有可能情况）。

4. 异常处理的好处：
   - 避免程序因异常而直接崩溃退出。
   - 可以向用户返回友好的错误提示信息，而不是晦涩的报错堆栈。
   - 让程序具备健壮性（鲁棒性），能优雅地处理意外情况。

5. 测试数据的设计思路：
   使用多组测试数据（正常、边界、异常），全面验证函数在各类情况下的表现。
   这是软件测试中常用的"等价类划分"方法。

6. 扩展思考：
   - 如果除数传入 0.0（浮点数零），结果会怎样？（提示：同样触发 ZeroDivisionError）
   - 如果传入 None 作为除数，会触发哪种异常？
   - 可以在 try 后面添加 else（无异常时执行）和 finally（无论是否异常都执行）子句。
"""