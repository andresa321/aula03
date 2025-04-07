#codigo para decifrar a logica e fazer um codigo para executar.

hora1 = int(input("digite a hora1: "))
minuto1 = int(input("digite o minuto1: "))

hora2 = int(input("digite a hora2: "))
minuto2 = int(input("digite o minuto2: "))

somahora = hora1 + hora2
somaminuto = minuto1 + minuto2

if somaminuto >= 60:
    somahora = somahora + 1
    somaminuto = somaminuto - 60

if somahora >= 24:
    somahora = somahora - 24
    print(f"{somahora}:{somaminuto:02d}")

if somahora >= 12:
     somahora = somahora - 12
     print(f"{somahora}:{somaminuto:02d}")