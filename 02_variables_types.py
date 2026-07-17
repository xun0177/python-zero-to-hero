"""
第2题：变量与数据类型
知识点：变量的定义与赋值、type() 函数查看数据类型、字符串、整数、布尔值
"""

def value_type():  # 定义一个函数，用于展示常见的数据类型
    # 定义四个变量，Python 会根据赋的值自动推断数据类型
    name = '我'          # 字符串类型（str），用引号包裹文本
    age = 18             # 整数类型（int），不带小数点的数字
    height = 180         # 整数类型（int），身高以厘米为单位
    is_student = True    # 布尔类型（bool），只有 True（真）或 False（假）两种值

    # type(变量) 返回该变量的数据类型，显示为 <class '类型'>
    print(f'姓名：{name}，数据类型：{type(name)}')        # <class 'str'>
    print(f'年龄：{age}，数据类型：{type(age)}')          # <class 'int'>
    print(f'身高：{height}，数据类型：{type(height)}')    # <class 'int'>
    print(f'学生：{is_student}，数据类型：{type(is_student)}')  # <class 'bool'>

# 调用函数，执行上述代码
value_type()


"""
补充说明

1. 四种常见基本数据类型：
   - 字符串（str）：用单引号或双引号包裹，如 '你好'、"Hello"
   - 整数（int）：正整数、负整数或零，如 -5、0、42
   - 浮点数（float）：带小数点的数，如 3.14、-0.5（本课未涉及但可了解）
   - 布尔值（bool）：逻辑值，只有 True 和 False 两种

2. type() 函数：
   用于检查变量或值的数据类型，调试时非常有用。

3. f-string 格式化：
   f'...{变量}...' 可以在字符串中直接嵌入变量值，是 Python 推荐的格式化方式。
"""