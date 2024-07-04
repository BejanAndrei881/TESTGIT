# try:
#     n = int(input("Introduceti numarul pentru suma:"))
#     suma = 0
#     i = 1
#     while i <= n:
#         suma = suma + i
#         i = i + 1
#     print(suma)
# except ValueError:
#     print("Numarul introdus nu este un intreg")
# try:
#     n = int(input("Introduceti un numar pentru a calcula numerele pare: "))

#     i = 1
#     suma = 0
#     while i <= n:
#         if i % 2 == 0:
#             suma = suma + i
#         i = i + 1
#     print(suma)
# except ValueError:
#     print("Numarul nu este integer")
    
lista_mea = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista_mea.sort()
print(lista_mea)
# lista_mea = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# list_pare=[]
# for x in lista_mea:
#     if x % 2 == 0:
#         list_pare.append(x)
# list_pare.sort()
# print(list_pare)
print(lista_mea[2::3])
