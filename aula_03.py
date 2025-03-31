#codigo para ler o nome de uma pessoa, a sua idade e seu salario no final.
nome=input("digite seu nome: ")
idade=int(input("digite sua idade: "))
salario=float(input("digite seu salario: "))
print(f"nome: {nome}\n"
      f"idade: {idade}\n"
      f"salario: {salario}\n")
percentual=int(input("insira o percentual do aumento: "))
aumento=(salario/100)* percentual

salarionovo=(salario+aumento)
print(salarionovo)
