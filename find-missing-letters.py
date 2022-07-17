import string
def find_missingl_etters(Givenletters:str):
    alpha = string.ascii_letters
    start = alpha.index(Givenletters[0]) #postion start
    for letters in alpha[start:]:
        if letters not in Givenletters:
            return letters

    return "no missing letters in squnase"

#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
case1 = find_missingl_etters("abcdf") #e
case2 = find_missingl_etters("mnopr") #q
case3 = find_missingl_etters("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #no missing letters
print(case1)
print(case2)
print(case3)


