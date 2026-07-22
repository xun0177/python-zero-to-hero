"""
第18题：装饰器（Decorator）
知识点：装饰器的定义与使用、*args 和 **kwargs 接收任意参数、@ 语法糖
"""

# ---------- 装饰器：自动添加点餐欢迎语和结束语 ----------
def ordering_decorator(func):  # 装饰器函数，参数是被装饰的函数
    """点餐装饰器：在点餐前后添加欢迎语和结束语"""
    
    def wrapper(*args, **kwargs):
        # 调用原函数之前执行的代码（前置增强）
        print("===== 🍔 欢迎光临，开始点餐 =====")
        
        # 调用原函数，并将所有参数原样传递进去
        result = func(*args, **kwargs)
        
        # 调用原函数之后执行的代码（后置增强）
        print("===== ✅ 点餐完成，请慢用！ =====")
        print()  # 输出空行分隔各次点餐
        
        return result  # 返回原函数的执行结果
    
    return wrapper  # 返回内部函数 wrapper


# ---------- 使用 @ 语法糖应用装饰器 ----------

# 函数1：没有参数
@ordering_decorator  # 等价于 order_cola = ordering_decorator(order_cola)
def order_cola():
    """点可乐"""
    print("🥤 一杯可乐")


# 函数2：有一个位置参数（数量）
@ordering_decorator
def order_fries(quantity):
    """点薯条"""
    print(f"🍟 {quantity}份薯条")


# 函数3：有位置参数和关键字参数（数量、口味）
@ordering_decorator
def order_burger(quantity, flavor="经典"):
    """点汉堡"""
    print(f"🍔 {quantity}个{flavor}汉堡")


# 函数4：只有关键字参数
@ordering_decorator
def order_chicken_wing(flavor="原味", quantity=1):
    """点鸡翅"""
    print(f"🍗 {quantity}份{flavor}鸡翅")


# ---------- 调用被装饰的函数 ----------
order_cola()                           # 无参数
order_fries(2)                         # 位置参数
order_burger(3, flavor="芝士")         # 位置参数 + 关键字参数
order_chicken_wing(flavor="香辣", quantity=4)  # 关键字参数


"""
补充说明

1. 装饰器的本质：
   - 装饰器是一个函数，它接收一个函数作为参数，并返回一个新的函数。
   - 被装饰的函数会被替换成装饰器返回的新函数。
   - 装饰器可以在不修改原函数代码的前提下，为函数增加额外功能。

2. @ 语法糖：
   - @decorator_name 是 Python 提供的便捷写法。
   - @ordering_decorator 等价于 order_cola = ordering_decorator(order_cola)
   - 语法糖让代码更简洁、可读性更强。

3. *args 和 **kwargs：
   - *args：接收所有位置参数，打包成元组（tuple）。
   - **kwargs：接收所有关键字参数，打包成字典（dict）。
   - 合在一起使用可以接收任意参数，让装饰器具有通用性。
   - 在 wrapper 内部调用原函数时，使用 *args 和 **kwargs 将参数原样传递。

4. 装饰器的执行流程：
   以 @ordering_decorator 装饰 order_cola 为例：
   - 定义 order_cola 函数。
   - 执行 order_cola = ordering_decorator(order_cola)
   - 调用 order_cola() 时，实际执行的是 wrapper() 函数。

5. 装饰器的典型应用场景：
   - 日志记录（记录函数调用信息）
   - 权限验证（检查用户是否有权限执行该操作）
   - 性能计时（计算函数执行耗时）
   - 缓存结果（避免重复计算）
   - 事务管理（数据库操作）

6. 命名优化说明：
   - 原装饰器名 点餐装饰器 改为 ordering_decorator（英文命名更规范）。
   - 原函数名 点可乐、点薯条、点汉堡、点鸡翅 改为 order_cola、order_fries、order_burger、order_chicken_wing（英文命名）。
   - 原参数名 份数 改为 quantity，口味 改为 flavor。
   - 原数量 改为 quantity，保持命名一致性。
   - 在面向国际的开源项目中，推荐使用英文命名，本教程后续题目也将统一使用英文命名。

7. 扩展思考：
   - 如何编写带参数的装饰器？（如 @repeat(times=3) 表示重复执行 3 次）
   - 多个装饰器同时装饰一个函数时，执行顺序是怎样的？
   - functools.wraps 装饰器的作用是什么？（保留原函数的元信息）
   - 类装饰器如何实现？
"""