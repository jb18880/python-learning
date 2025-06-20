"""
通过type()语句输出字面量的数据类型

| 中文名 | 英文名 / Python 类型     | 示例                     |
| --- | ------------------- | ---------------------- |
| 整数  | Integer (`int`)     | `a = 10`               |
| 浮点数 | Float (`float`)     | `b = 3.14`             |
| 字符串 | String (`str`)      | `name = "Alice"`       |
| 布尔值 | Boolean (`bool`)    | `is_active = True`     |
| 列表  | List (`list`)       | `nums = [1, 2, 3]`     |
| 元组  | Tuple (`tuple`)     | `t = (1, 2, 3)`        |
| 集合  | Set (`set`)         | `s = {1, 2, 3}`        |
| 字典  | Dictionary (`dict`) | `d = {"a": 1, "b": 2}` |
| 空值  | NoneType (`None`)   | `x = None`             |

"""

# 使用print语句直接输出数据类型信息
# 输出字符串的数据类型
print(type("python真好玩啊，python真简单啊"))
# 输出整数的数据类型
print(type(666))
# 输出浮点数的数据类型
print(type(3.14))



# 先用变量存储type()的结果，再输出变量值，间接输出数据类型的信息
# 使用变量存储数据类型的值
string_type = type("python好啊，python得学啊")
int_type= type(666)
float_type= type(3.14)
# 输出三个变量的值
print(string_type)
print(int_type)
print(float_type)


# 使用type()语句查看变量中存储的数据类型信息
sentense = "Hello World"
sentense_type = type(sentense)
print(sentense_type)