valor_combustível = float(input("Qual valor de combústivel você gostaria de consultar? "))

print(f"O valor do combustível é: {valor_combustível}")

valor_abastecimento = float(input("Qual o valor a ser abastecido? "))

print(f"O valor a ser abastecido é: {valor_abastecimento}")

valor_litros = valor_abastecimento / valor_combustível

print(f"O total a ser abastecido seria: {valor_litros:.2f} Litros")
