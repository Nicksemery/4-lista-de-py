# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
    # 1. Para homens: (72.7*h) - 58
    # 2. Para mulheres: (62.1*h) - 44.7

h = float(input("Qual sua altura? "))
info = input("Você é homem ou mulher? ")
calh = (72.7 *h) - 58
calm = (62.1 *h) - 44.7
if info == "homem" or "Homem" :
    print(f"Seu peso ideal é {calh}")
elif info == "mulher" or "Mulher" :
    print(f"Seu peso ideal é {calm}")