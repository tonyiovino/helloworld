import math

print("Ti calcorerò la superficie e il volume di una sfera!")
r = input("Inserisci il raggio! ")
r = int(r)

superficie = 4. * math.pi * r * r
volume = 4. / 3. * math.pi * r * r * r

print("La sfera di raggio", r, "ha superficie", superficie, "e volume", volume)