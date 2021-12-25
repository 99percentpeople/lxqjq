from dataType import *

def 获取编号(_编号表: list) -> int:
    i = 1
    while True:
        try:
            _编号表.index(i)
        except:
            break
        else:
            i += 1
    return i


    