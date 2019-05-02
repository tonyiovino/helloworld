import math

print("Digitare 1 se si vuole sapere il volume di un cubo, 2 se si vuole sapere quello della sfera.")
scelta = input("Numero 1 o 2? ")

if scelta==1:
    print("Scrivi il nunero del lato e ti calcolerò il volume del cubo!")

    num = input("Numero: ")
    num = int(num)

    volume = num * num * num

    print("Il volume di", num, "è", volume)
else scelta==2:
    print("Ti calcorerò la superficie e il volume di una sfera!")
    r = input("Inserisci il raggio! ")
    r = int(r)

    superficie = 4. * math.pi * r * r
    volume = 4. / 3. * math.pi * r * r * r

    print("La sfera di raggio", r, "ha superficie", superficie, "e volume", volume)
