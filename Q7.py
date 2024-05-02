# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # 1. o produto do dobro do primeiro com metade do segundo .
    # 2. a soma do triplo do primeiro com o terceiro.
    # 3. o terceiro elevado ao cubo.

in1 = int(input("Me dê um número inteiro: "))
in2 = int(input("Me dê outro número inteiro: "))
re = float(input("Agora um real: "))
cal1 = (in1 *2)*(in2/2)
cal2 = (in1 *3) + re
cal3 = re **3
print(cal1) # 1.
print(cal2) # 2.
print(cal3) # 3.