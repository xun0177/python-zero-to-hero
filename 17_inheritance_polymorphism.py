"""
第17题：继承与多态（面向对象进阶）
知识点：父类与子类、super() 调用父类方法、方法重写、多态
"""

# ---------- 父类：宠物（公共特征集中管理） ----------
class Pet:
    """宠物基类，定义所有宠物共有的属性和方法"""
    
    def __init__(self, name, age, owner):
        """构造方法，初始化宠物的基本信息"""
        self.name = name      # 宠物名字
        self.age = age        # 宠物年龄
        self.owner = owner    # 宠物主人
    
    def introduce(self):
        """返回宠物的自我介绍信息"""
        return f"{self.name}，{self.age}岁，主人是{self.owner}"


# ---------- 子类：狗（继承 Pet） ----------
class Dog(Pet):  # 括号内写 Pet，表示 Dog 继承自 Pet 类
    """狗类，继承自 Pet，增加狗特有的属性和方法"""
    
    def __init__(self, name, age, owner, breed):
        # super() 调用父类的 __init__ 方法，初始化公共属性
        super().__init__(name, age, owner)
        self.breed = breed  # 狗特有的属性：品种
    
    def sound(self):
        """狗特有的叫声方法"""
        return "汪汪！"
    
    # 重写父类的 introduce 方法，在原有信息基础上追加品种信息
    def introduce(self):
        # super().introduce() 调用父类的方法，获取公共信息
        return super().introduce() + f"，品种：{self.breed}"


# ---------- 子类：猫（继承 Pet） ----------
class Cat(Pet):  # 继承自 Pet 类
    """猫类，继承自 Pet，增加猫特有的属性和方法"""
    
    def __init__(self, name, age, owner, color):
        # 调用父类构造方法初始化公共属性
        super().__init__(name, age, owner)
        self.color = color  # 猫特有的属性：毛色
    
    def sound(self):
        """猫特有的叫声方法"""
        return "喵喵！"
    
    # 重写父类的 introduce 方法，在原有信息基础上追加毛色信息
    def introduce(self):
        return super().introduce() + f"，毛色：{self.color}"


# ---------- 创建对象（实例化子类） ----------
dog = Dog("旺财", 3, "小明", "金毛")  # 创建狗对象，传入狗所需的全部参数
cat = Cat("咪咪", 2, "小红", "白色")  # 创建猫对象，传入猫所需的全部参数

# ---------- 调用子类的方法 ----------
print(dog.introduce())  # 输出：旺财，3岁，主人是小明，品种：金毛
print(dog.sound())      # 输出：汪汪！
print(cat.introduce())  # 输出：咪咪，2岁，主人是小红，毛色：白色
print(cat.sound())      # 输出：喵喵！

print()  # 输出空行

# ---------- 多态：统一处理不同子类的对象 ----------
pets = [dog, cat]  # 将不同子类的对象放入同一个列表
for pet in pets:   # 遍历列表，统一调用相同名称的方法
    # 虽然调用的是同名方法（introduce 和 sound），
    # 但每个对象会执行各自类中重写后的版本——这就是多态
    print(pet.introduce(), "叫声：", pet.sound())


"""
补充说明

1. 继承（Inheritance）：
   - 子类（Dog、Cat）继承父类（Pet）的所有属性和方法。
   - 子类可以重用父类代码，减少重复编写。
   - 语法：class 子类名(父类名):

2. super() 函数：
   - 用于调用父类的方法。
   - super().__init__(...)：调用父类的构造方法，初始化公共属性。
   - super().introduce()：调用父类的 introduce 方法，获取公共信息。
   - 使用 super() 可以避免硬编码父类名称，在多重继承时也更安全。

3. 方法重写（Override）：
   - 子类可以定义与父类同名的方法，覆盖父类的实现。
   - 本例中 Dog 和 Cat 都重写了 introduce 方法。
   - 重写后，调用子类对象的该方法时，执行的是子类版本的代码。

4. 多态（Polymorphism）：
   - 同一操作（如 pet.introduce()）作用于不同对象时，表现出不同的行为。
   - 本例中：dog.introduce() 输出带品种的信息，cat.introduce() 输出带毛色的信息。
   - 多态让代码更灵活：循环遍历 pets 列表时，无需判断对象类型，直接调用即可。

5. 类之间的关系：
   - 继承关系（is-a）：狗是一种宠物（Dog is a Pet）。
   - 子类拥有父类的全部特征，并可以扩展自己的特有特征。

6. 命名优化说明：
   - 原有命名已非常规范，无需修改。
   - 类名使用大驼峰（Pet、Dog、Cat），方法名使用蛇形命名法。
   - 变量名 dog、cat、pets 清晰表达含义。

7. 扩展思考：
   - 如果再增加一个子类 Bird（鸟），需要实现哪些方法？
   - 如果父类 Pet 有多个子类，能否将 pets 列表中的对象按某种规则排序？
   - 什么是多重继承？Python 支持多重继承吗？（提示：支持，如 class A(B, C):）
   - 如果子类不重写 introduce 方法，调用时会发生什么？（提示：调用父类版本）
"""