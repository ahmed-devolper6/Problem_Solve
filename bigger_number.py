
def sreval_num(number):
    res = [int(x ) for x  in str(number)]
    biggest_num = 0 
    for number in res:
        if number > biggest_num:
            number = biggest_num
            bad = biggest_num 
    return res


print(sreval_num(50545155552152525))