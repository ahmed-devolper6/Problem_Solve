def find_long_string(sequnse):
    global count
    count =  0
    liststing = sequnse.split(" ")
    for word in liststing:
       if len(word) > count:
        count = len(word)
        longest = word
    return word
seq = find_long_string("is ahmedjamal dfgdfgdfgfdgfdgdfgdf")
print(seq)