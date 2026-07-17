"""
第9题：字符串常用方法
知识点：strip() 去除两端空格、upper() 转大写、lower() 转小写、
       title() 首字母大写、replace() 替换子串、split() 分割、
       join() 连接、find() 查找子串位置
"""

# 定义原始字符串作为示例数据
original_text = 'hello, python world.'  # 注意：这里前后没有空格，但 strip() 依然可用

def string_operations_demo():  # 函数名清晰表达"字符串操作演示"的功能
    """演示 Python 中常用的字符串方法"""
    print(f'原字符串：{original_text}')
    
    # ---------- 去除空白字符 ----------
    # strip() 去除字符串两端（开头和结尾）的空白字符（空格、制表符、换行符等）
    # 原字符串开头和结尾没有空格，所以结果看起来与原字符串相同
    print(f'去两端空格：{original_text.strip()}')
    
    # ---------- 大小写转换 ----------
    print(f'转大写：{original_text.upper()}')   # 所有字母转换为大写
    print(f'转小写：{original_text.lower()}')   # 所有字母转换为小写
    print(f'首字母大写：{original_text.title()}')  # 每个单词首字母大写（标题格式）
    
    # ---------- 替换和分割 ----------
    # replace(old, new) 将指定的旧子串替换为新子串
    print(f'java替换python：{original_text.replace("python", "java")}')
    
    # split() 默认按空白字符（空格、换行、制表符）分割字符串，返回列表
    # 对原字符串分割会得到 ['hello,', 'python', 'world.']
    print(f'分割：{original_text.split()}')
    
    # join() 将可迭代对象（如列表）中的元素用指定字符连接成新字符串
    # 先用 split() 分割成列表，再用 "-" 连接成新字符串
    print(f'用-连接：{"-".join(original_text.split())}')
    
    # ---------- 查找 ----------
    # find(sub) 返回子串在原字符串中第一次出现的索引位置，找不到返回 -1
    print(f'查找python：{original_text.find("python")}')

# 调用函数执行演示
string_operations_demo()


"""
补充说明

1. 字符串的不可变性：
   所有字符串方法都不会修改原字符串，而是返回一个新的字符串。
   （因为 Python 中字符串是不可变类型）

2. 常用去除空白方法：
   - strip()：去除两端的空白字符。
   - lstrip()：只去除左端（开头）的空白字符。
   - rstrip()：只去除右端（末尾）的空白字符。

3. 大小写转换方法：
   - upper()：所有字母转大写（如 "hello" -> "HELLO"）。
   - lower()：所有字母转小写（如 "HELLO" -> "hello"）。
   - title()：每个单词首字母转大写（如 "hello world" -> "Hello World"）。
   - capitalize()：仅第一个字符大写（如 "hello" -> "Hello"）。

4. replace() 方法：
   - replace(old, new) 将字符串中的所有 old 替换为 new。
   - 可以指定第三个参数 count，限制替换次数（如 replace("a", "b", 2) 只替换前 2 个）。

5. split() 和 join()：
   - split() 将字符串分割为列表，常用于处理以空格或特定分隔符分隔的数据。
   - join() 将列表合并为字符串，是 split() 的逆操作。
   - 两者配合使用是字符串处理的常用模式。

6. find() 方法：
   - 返回子串第一次出现的索引（从 0 开始计数）。
   - 找不到时返回 -1（与 index() 不同，index() 找不到会报错）。
   - 也可以指定搜索范围：find(sub, start, end)。

7. 命名优化说明：
   原变量名 text 改为 original_text，更明确地表示"原始字符串"，
   避免在后续操作中与处理后的字符串产生混淆。

8. 扩展思考：
   如果字符串中包含多个空格或制表符，split() 会如何处理？
   （提示：split() 会连续多个空白字符视为一个分隔符）
"""