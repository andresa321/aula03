# aula03
nome=input("digite seu nome: ")
idade=int(input("digite sua idade: "))
salario=float(input("digite seu salario: "))
print(f"{nome}\n tem {idade}\n anos e recebe {salario}\n por mes. ")

if media >= 7.0:
    print(f"aprovado {media}")
elif media < 4:
    print("reprovado")
else:
    print("recuperacao")