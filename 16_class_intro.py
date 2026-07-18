"""
第16题：类与对象（面向对象编程入门）
知识点：类的定义、__init__ 构造方法、self 参数、创建对象、调用方法
"""

class Student:  # 类名使用大驼峰命名法（每个单词首字母大写）
    """学生类，用于存储学生信息并提供信息输出方法"""
    
    def __init__(self, name, age, gender):
        """
        构造方法（初始化方法），在创建对象时自动调用
        用于为对象设置初始属性值
        """
        self.name = name      # 将参数 name 赋值给实例属性 self.name
        self.age = age        # 将参数 age 赋值给实例属性 self.age
        self.gender = gender  # 将参数 gender 赋值给实例属性 self.gender
    
    def get_name(self):  # 实例方法的第一个参数必须是 self（代表实例本身）
        """返回学生的姓名"""
        return f"我的名字是{self.name}；"
    
    def get_age(self):  # 方法名使用蛇形命名法（全小写，下划线分隔）
        """返回学生的年龄"""
        return f"我的年龄是{self.age}岁；"
    
    def get_gender(self):
        """返回学生的性别"""
        return f"我的性别是{self.gender}。"


# ---------- 创建对象（实例化） ----------
# 类名后加括号，传入 __init__ 所需的参数，返回一个实例对象
student1 = Student("小明", 18, "男")  # 创建一个名为"小明"的学生对象
student2 = Student("小红", 20, "女")  # 创建一个名为"小红"的学生对象

# ---------- 调用对象的方法 ----------
# 使用 对象.方法名() 的语法调用方法，self 会自动传入（无需手动）
print(student1.get_name())
print(student1.get_age())
print(student1.get_gender())
print()  # 输出空行，分隔两组结果
print(student2.get_name())
print(student2.get_age())
print(student2.get_gender())


"""
补充说明

1. 类（class）与对象（object）：
   - 类是创建对象的模板（蓝图），定义了对象的属性和方法。
   - 对象是类的具体实例（根据模板创建出来的实体）。
   - 同一个类可以创建多个不同的对象。

2. __init__ 构造方法：
   - 特殊方法，名称前后各有两个下划线。
   - 在创建对象时自动调用，用于初始化对象的属性。
   - 第一个参数必须是 self（代表当前正在创建的对象）。

3. self 关键字：
   - 代表实例本身，是实例方法的第一个参数。
   - 通过 self 可以访问该实例的属性（self.name）和其他方法。
   - 调用方法时不需要传递 self，Python 会自动传入。

4. 实例属性与实例方法：
   - 属性：在 __init__ 中通过 self.属性名 = 值 定义，属于每个对象独立的数据。
   - 方法：在类中定义的函数，第一个参数为 self，属于每个对象共享的行为。

5. 命名优化说明：
   - 原类名 woa 改为 Student（类名用大驼峰，清晰表达"学生"）。
   - 原方法名 myname、myage、mygender 改为 get_name、get_age、get_gender（更规范）。
   - 原对象名 sg1、sg2 改为 student1、student2（更清晰）。

6. 类与对象的关系比喻：
   - 类 = 饼干模具（设计图），对象 = 饼干（成品）。
   - 一个模具可以压出无数块饼干，每块饼干都有自己的形状，但都遵循同一个设计。

7. 扩展思考：
   - 如何为类添加一个新方法，如 introduce()，一次性输出所有信息？
   - 如何修改对象的属性值？例如 student1.age = 19
   - 如果 __init__ 中的参数有默认值，该如何定义？
   - 是否可以创建不包含任何属性和方法的空类？（可以，用 pass 占位）
"""