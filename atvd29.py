# Exercício Python 29: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
p = [ ]
maior = 0 
menor = 0

for l in range (0, 5):
    peso = float(input(" digite :"))
    p.append(peso)
    peso2 = sorted(p)
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            if peso < maior: 
                menor = peso 

print(f"""o menor peso é : {peso2[0]} \n o maior peso é : {peso2[4]} """)