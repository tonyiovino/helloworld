import math

print("Ti calcolerò 'AX^2 + BX + C = 0'!")
print("Inserisci i valori")

A = input("Inserisci il valore assunto da A: ")
A = int(A)

B = input("Inserisci il valore assunto da B: ")
B = int(B)

C = input("Inserisci il valore assunto da C: ")
C = int(C)

if A==0 and B==0 and C==0:
	print("L'equazione 0 = 0 ha infinite soluzioni")

elif A==0 and B==0:
	print("L'equazione", C, "= 0 non ha soluzioni")

elif A==0:
	print("L'equazione", B, "+", C, "= 0 non ha soluzioni")

else:
	X = -B -sqrt(B * B -4 * A * C) / 2 * A
	X = -B +sqrt(B * B -4 * A * C) / 2 * A