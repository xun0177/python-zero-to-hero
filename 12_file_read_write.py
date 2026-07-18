"""
第12题：文件读写操作
知识点：with open() 上下文管理器、文件写入模式 'w'、文件读取模式 'r'、
       encoding='utf-8' 编码设置、异常捕获处理
"""

def file_read_write_demo():  # 函数名清晰表达"文件读写演示"的功能
    # ---------- 准备文件数据 ----------
    filename = "12_file.txt"  # 文件名（如果不存在，写入模式会自动创建）
    file_content = "这是一段字符串，我准备用于写入文件。"  # 要写入的文本内容

    try:
        # ---------- 写入文件 ----------
        # with open() 是上下文管理器，会自动关闭文件（即使发生异常也会关闭）
        # 'w' 表示写入模式：文件存在则覆盖，不存在则创建
        # encoding='utf-8' 确保中文字符正确存储
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(file_content)  # 将字符串写入文件
        print(f"内容已成功写入文件{filename}。")

        # ---------- 读取文件 ----------
        # 'r' 表示只读模式：文件必须存在，否则会触发 FileNotFoundError
        with open(filename, 'r', encoding='utf-8') as file:
            read_content = file.read()  # read() 一次性读取文件全部内容
        print(f"文件{filename}的内容为：[{read_content}]")

    except Exception as error:  # 捕获所有类型的异常（通用异常处理）
        # 实际开发中建议捕获具体异常，这里为了演示统一处理
        print(f"文件操作错误：{error}")

# 调用函数执行文件读写演示
file_read_write_demo()


"""
补充说明

1. with open() 上下文管理器：
   - 使用 with 语句打开文件，Python 会自动管理文件的打开和关闭。
   - 即使写入或读取过程中发生异常，文件也会被正确关闭。
   - 比手动调用 f.close() 更安全、更简洁。

2. 文件打开模式：
   - 'w'（write）：写入模式，文件存在则覆盖，不存在则创建。
   - 'r'（read）：只读模式，文件必须存在，否则抛出 FileNotFoundError。
   - 'a'（append）：追加模式，在文件末尾追加内容，文件不存在则创建。
   - 'w+'、'r+' 等读写混合模式（本例未涉及）。

3. encoding='utf-8' 编码设置：
   - 指定文件的字符编码为 UTF-8，确保中文等非 ASCII 字符能正确读写。
   - 如果不指定编码，Windows 系统默认使用 GBK，可能导致中文乱码。
   - 推荐始终显式指定 encoding='utf-8'。

4. file.read() 方法：
   - 一次性读取文件的全部内容，返回字符串。
   - 如果文件很大，不建议一次性读取，会占用大量内存。
   - 大文件建议使用 readline() 逐行读取或 readlines() 读取所有行（返回列表）。

5. 异常处理：
   - 本例使用 except Exception as error 捕获所有可能的异常。
   - 通用捕获可以防止程序崩溃，但会掩盖具体错误类型。
   - 实际开发中建议分别捕获 FileNotFoundError、PermissionError 等具体异常。

6. 文件操作的两步流程：
   - 写入：先准备内容，再写入文件。
   - 读取：先打开文件，再读取内容。
   - 通常写入和读取是独立操作，本例放在一起是为了演示完整的读写流程。

7. 扩展思考：
   - 如果文件不存在，但使用 'r' 模式读取会发生什么？（提示：FileNotFoundError）
   - 如果连续调用两次写入，文件内容会怎样？（提示：'w' 模式会覆盖）
   - 如何在不覆盖原有内容的情况下追加新内容？（提示：使用 'a' 模式）
   - 如果文件路径包含多层文件夹（如 "data/12_file.txt"），需要注意什么？
"""