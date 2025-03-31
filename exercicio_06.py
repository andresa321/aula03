#codigo para dois times e o numero de gols marcado na partida e escrever o nome do vencedor.
time1=input("digite o primeiro time: ")
time2=input("digite o segundo time: ")

goltime1=int(input("digite o numero do gol: "))
goltime2=int(input("digite o numero do gol: "))

if goltime1 > goltime2:
    print(f"o {time1} foi vencedor da partida obvio pois ele é o melhor. ")
else:
    if goltime2 > goltime1:
        print(f"o {time2} foi o vencedor")
    else:
        print("empate")


