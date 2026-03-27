diaria_pedreiro = float(input("Qual foi a quantidade de dias trabalhados deste pedreiro: "))
print(f"A quantidade de dias trabalhados deste pedreiro foi: {diaria_pedreiro}")
print(f"A diaria deste pedreiro custa R$150")
salario_pedreiro = (diaria_pedreiro * 150)
print(f"O salario deste pedreiro é: {salario_pedreiro}")

porcentagem_inss = (salario_pedreiro * 0.07)
desconto_inss = (salario_pedreiro - porcentagem_inss)
print (f"O salario do pedreiro com o desconto do inss é: R${desconto_inss}")

porcentagem_ir = (salario_pedreiro * 0.15)
desconto_ir = (salario_pedreiro - porcentagem_ir)
print (f"O salário do pedreiro com o desconto do Ir é: R${desconto_ir}")

todos_descontos = (salario_pedreiro - (porcentagem_inss + porcentagem_ir))
print(f"Com os descontos o salário deste pedreiro é: {todos_descontos}")