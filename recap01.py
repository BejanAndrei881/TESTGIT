#Liste functii
# lista_mea = [5, 4, "ana are", 10, 8, "Thor", 10, 10]
# print(lista_mea[0:3])\
# print(lista_mea.index("Thor"))
# lista_mea.append(True)
# lista_mea.insert(2, 99)
# print(lista_mea)
# lista_mea.remove(99)
# print(lista_mea)
# lista_mea.pop(2)
# lista_mea.clear()
# lista_mea.reverse()
# lista_mea.sort()
# lista_mea.count(10)
# print(lista_mea.count(10))

#Tupluri
#ezz
#Dictionare

# def sum_nb(x,y):
#     try:
#         if x == y:
#             return "Error number not should be equal"
#         sum = 0
#         if x <  y:
#             while x <= y:
#                 sum += x
#                 x += 1

#         else:
#             while x >= y:
#                 sum = sum + y
#                 y = y +1
#         return sum
#     except TypeError:
#         print("CE ATI INTRODUS NU SUNT NUMERE")
# print(sum_nb(-1,"ana"))

# def n_fac(n):
#     try:
#         factorial = 1
#         if n == 0  or n==1:
#             factorial = 1

#         if n > 0:
#             while n >= 1:
#                 factorial = factorial * n
#                 n -= 1
#             return factorial

#         else:
#             return "ERROR MESSAGE"
        
#     except TypeError:
#         return "Nu ati introdus numere"

# print(n_fac("ana"))

def show_arr(a):

    x = len(a)
    if x > 0 :
        for i in range(x):
            print(a[i])
    else:
        print(a)

# a = [4, 9, 0]
a=[-1,-2,-3]
show_arr((a))        