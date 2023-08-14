'''
3) Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

alt = input("Olá, qual é a sua altura?")
peso = int(input("E qual é o seu peso?"))

conta = alt*100
cont = peso*1000

print(f"Sua altura em centímetros é {conta}")
print(f"Seu peso em gramas é {cont}")