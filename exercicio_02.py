#codigo para ler dois numeros e efetuar as quatro operacoes matematicas
numero1=float(input("digite o numero: "))
numero2=float(input("digite o numero: "))

soma= numero1+numero2
divisao= numero1/numero2
subtracao= numero1-numero2
multiplicacao= numero1*numero2

print(f"{numero1} + {numero2} é igual a{soma}\n"
      f"{numero1} - {numero2} é igual a {subtracao}\n "
      f"{numero1} /{numero2} é igual a {divisao}\n "
      f"{numero1} * {numero2} é igual a {multiplicacao}\n. ")

