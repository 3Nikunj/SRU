# String: Anything within single or double quotation is a string

# s = "Nikunj sondawale"

# print(s.swapcase())

# print(s.title())

# print(s.startswith('n'))
# print(s.endswith('e'))

# print(s.upper(), s.lower())


s = "Nikunj sondawale"

# print(s.count('a'))
# # print(s.index('z'))
# print(s.find('z'))


# fruits = "apple,kiwi,mango,orange"
# lt = fruits.split('a')
# print(lt)

# s1 = "  nikunj "
# print(s1)
# print(s1.strip())

# s1 = "Nikunj"
# s2 = "Lekhrao"
# s3 = "Sondawale"

# z = s1+s2+s3
# print(z)


# s = 'nikunj'
# print(s.isdigit())

# print(s.isalnum())

# print(s.isspace())

# print(s.isalpha())


# s = "nikunj"
# print(len(s))

# z = str(123)
# print(type(z))

# z = str(False)
# print(type(z))





s = "01.01.01.01"
s1 = "52.0.45.147"

def isValid(s):
    split_s = s.split('.')    # ['222','111','111','111']
    if len(split_s) != 4:
        return False
    
    for i in split_s:
        if len(i)!=1 and i[0] == '0':
            return False
        if not i.isdigit():
            return False
        if int(i)<0 or int(i)>255:
            return False
    return True

isValid(s)