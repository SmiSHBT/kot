#1

# a = [1, 2, 32, 67, 33, 3, 2, 7, 90]
# for x in a:
#     if x < 5:
#         print(x)

#2

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [1, 2, 43, 322, 21, 34, 56]
# c = list(set(a) & set(b))
# print(c)

#3 

# a = {
#     'a': 500,
#     'b': 5870,
#     'c': 6000,
#     'd': 4000,
#     'e': 8938,
# }

# c= sorted(a.items(), key=lambda item: item[1], reverse=True)

# b= [item[0] for item in c[:3]]

# print(b)

#4

# a = "botalo xich narsa bilmidi "
# b = 'b'
# c = a.count(b)
# print(f"simvol-'{b}' , poyavlyaetsa {c} raz(a).")

#5

# import random

# a = random.randint(1,100)
# b = int(input("ugadayte chislo: "))

# if a == b:
#     print('VI UGADALI!')
# elif b > a:
#     print('zagadannoye chislo menshe chem vash')
#     b = int(input("poprobuyte eshe raz: "))
# elif a > b:
#      print('zagadannoye chislo bolshe chem vash')
#      b = int(input("poprobuyte eshe raz: "))

#6

# a = int(input("vvedite 1 chislo: "))
# b = int(input("vvedite 2 chislo: "))
# c = str(input("vvedite znak: "))
# if c == "+":
#     print(a + b)
# elif c == "-":
#     print(a - b)
# elif c == "/":
#     print(a / b)
# elif c == "*":
#     print(a * b)

#7

# def check_odd(a):
#     if a % 2 == 0:
#         print(" chislo chetnoye")
#     else:
#         print(" chislo ne chetnoye")

# b = int(input("vvedite chislo: "))
# check_odd(b)

#8

# def sum_list(c):
#     a= 0
    
#     for x in c:
#         a += x
    
#     return a

# v = [1, 2, 3, 4, 5]
# print(sum_list(v))