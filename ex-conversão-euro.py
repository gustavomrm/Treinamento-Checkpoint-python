valor_reais = float(input("Digite o valor em reais que você deseja converter: "))
print(f"O valor em reais que será convertido será: R${valor_reais}")

print("1 Euro atualmente vale 6.05 reais")
valor_conversao = (valor_reais / 6.05)
print(f"O valor da conversão de reais para euros é: {valor_conversao:.2f}")
