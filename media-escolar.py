media_p1 = float(input("Digite a nota da primeira prova: "))
print(f"A primeira nota é: {media_p1}")

media_p2 = float(input("Digite a nota da segunda prova: "))
print(f"A segunda nota é {media_p2}")

media_p3 = float(input("Digite a nota da terceira prova: "))
print(f"A terceira nota é: {media_p3}")

media_final = (media_p1 * 0.2) + (media_p2 * 0.2)  + (media_p3 * 0.6)
print(f"A sua média final é: {media_final:.2f}")