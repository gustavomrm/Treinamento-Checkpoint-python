valor_produto = float(input("Digite o valor do produto: "))

desconto = (0.05 * valor_produto)

valor_final = (valor_produto - desconto)
print(f"O desconto do produto é de 5%")
print(f"O valor final do produto é: {valor_final} ")
print(f"O valor do produto antes do desconto é: R${valor_produto} e o desconto aplicado no produto é de R${desconto} ")
