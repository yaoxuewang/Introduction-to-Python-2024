##通过测试，可确定代码面对各种输入都能够按要求工作。测试让你坚信，无论有多少人使用你的程序，它都将正确地工作。
#在程序中添加新代码时，也可对其进行测试，确认它们不会破坏程序既有的行为。

#11.2 测试函数
#11.2.1 单元测试和测试用例
#单元测试（unit test），用于核实函数的某个方面没有问题
#测试用例（test case）是一组单元测试，这些单元测试一道核实函数在各种情况下的行为都符合要求

#11.2.2 可通过的测试
from name_function import get_formatted_name
def test_first_last_name():
    """能够正确地处理像 Janis Joplin 这样的姓名吗？"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

#11.2.4 未通过的测试
def get_formatted_name(first, middle, last):
"""生成格式规范的姓名"""
full_name = f"{first} {middle} {last}"
return full_name.title()

#11.2.6 添加新测试
from name_function import get_formatted_name
def test_first_last_name():
"""能够正确地处理像 Janis Joplin 这样的姓名吗？"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
def test_first_last_middle_name():
    """能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名吗？"""
    formatted_name = get_formatted_name(
    'wolfgang', 'mozart', 'amadeus')
assert formatted_name == 'Wolfgang Amadeus Mozart'