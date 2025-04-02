#codigo para escrever um algoritimo que leia o numero de litros vendidos e o tipo de combustivel.

qtdlitros=float(input("digite a quantidade de combustivel:"))
tipo=input("se o combustivel for gasolina digite G ou se for etanol digite E\n:")

vgasolina= 5.80
vetanol= 4.90

if tipo == "g" or tipo == "G":
    gcalculo= qtdlitros*vgasolina
    print(f"voce abateceu com gasolina e gastou {gcalculo}: ")

elif tipo == "e" or tipo == "E":
    ecalculo= qtdlitros*vetanol
    print(f" voce abateceu com enatnol e gastou {ecalculo}: ")

else:
    print("solicitacao invalida.")
