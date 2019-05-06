print("EQUAZIONI PRIMO GRADO")
print("ax + b = 0")

A = input("A: ")
A = int(A)
B = input("B: ")
B = int(B)

if A==0 and B==0:
    print("L'equazione 0 = 0 ha infinite soluzioni")

elif A==0:
    print("L'equazione", B, "= 0 non ha soluzioni")

else:
    x = -B / A
print("L'equazione ha soluzione:", x)