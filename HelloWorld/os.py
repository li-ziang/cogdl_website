import os

def operation(cmd):
    res = os.popen(cmd)
    print(cmd)
    output_str = res.read()   # 获得输出字符串
    return output_str