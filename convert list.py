def convert_num(number:int):
    resualt = []
    for x in str(number):
        resualt.insert(0,int(x))    

    return resualt


print(convert_num(541541547245))