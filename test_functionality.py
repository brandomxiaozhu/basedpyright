# 测试BasedPyright类型检查功能

def add_numbers(a: int, b: int) -> int:
    """添加两个整数"""
    return a + b

def greet(name: str) -> str:
    """问候函数"""
    return f"Hello, {name}!"

# 正确的用法
result = add_numbers(1, 2)
greeting = greet("World")

# 故意的类型错误，用于测试类型检查
wrong_result = add_numbers("hello", "world")  # 应该报错：传入字符串而不是整数
wrong_greeting = greet(123)  # 应该报错：传入整数而不是字符串

# 未定义变量错误
print(undefined_variable)  # 应该报错：未定义的变量

# 类型注解测试
from typing import List, Dict, Optional

def process_list(items: List[str]) -> Dict[str, int]:
    """处理字符串列表，返回字符串长度字典"""
    return {item: len(item) for item in items}

def find_user(user_id: int) -> Optional[str]:
    """根据ID查找用户"""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# 测试复杂类型
string_list = ["hello", "world"]
lengths = process_list(string_list)

# 错误的类型使用
wrong_lengths = process_list([1, 2, 3])  # 应该报错：传入整数列表而不是字符串列表

print(f"Results: {result}, {greeting}")
print(f"Lengths: {lengths}")