"""
 这个文件是做数据类型转换用的
"""
from encodings.punycode import insertion_unsort

# 将数字转换成字符串
num_str = str(11)
print(type(num_str),num_str)
float_str = str(10.11)
print(type(float_str),float_str)

# 将字符串转换成数字
num1 = int("11")
print(type(num1),num1)

num2 = float(2.33)
print(type(num2),num2)

# 整数转浮点数
float_num = float(122)
print(type(float_num),float_str)

# 浮点数转整数
int_num = int(19.093)
print(type(int_num),int_num)