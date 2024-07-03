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
try:
    n = int(input("Introduceti un numar pentru a calcula numerele pare: "))

    i = 1
    suma = 0
    while i <= n:
        if i % 2 == 0:
            suma = suma + i
        i = i + 1
    print(suma)
except ValueError:
    print("Numarul nu este integer")
    
