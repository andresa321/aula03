#codigo receber 3 notas de um aluno e verificar se ele esta reprovado ou aprovado.

nota1=float(input("digite a nota 1: "))
nota2=float(input("digite a nota 2: "))
nota3=float(input("digite a nota 3: "))

media=(nota1+nota2+nota3)//3

if media >= 7.0:
    print(f"aprovado {media}")
else:
    print(f"reprovado {media}")
