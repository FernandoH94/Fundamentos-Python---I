print("Cálculo de IMC")

peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))

calculo = peso / (altura ** 2)

print(f"O seu IMC é {calculo}")
