import random


tipos = ["tréboles", "corazones", "diamantes", "picas"]
numeros = list(range(1, 14))


mazo = []
for tipo in tipos:
    for numero in numeros:
        mazo.append((tipo, numero))


random.shuffle(mazo)

print("Mazo desordenado:")
for carta in mazo:
    print(carta)

print("\n----------------------------\n")


peso_tipo = {
    "tréboles": 1,
    "corazones": 2,
    "diamantes": 3,
    "picas": 4
}


for i in range(1, len(mazo)):
    carta_actual = mazo[i]
    j = i - 1

    while j >= 0 and (
        peso_tipo[mazo[j][0]] > peso_tipo[carta_actual[0]] or
        (peso_tipo[mazo[j][0]] == peso_tipo[carta_actual[0]] and mazo[j][1] > carta_actual[1])
    ):
        mazo[j + 1] = mazo[j]
        j -= 1

    mazo[j + 1] = carta_actual

print("Mazo ordenado:")
for carta in mazo:
    print(carta)