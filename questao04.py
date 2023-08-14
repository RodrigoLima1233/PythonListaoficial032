'''
4) Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros
'''
import math

alt = float(input("Olá, qual é a sua altura?"))
peso = float(input("E qual é o seu peso?"))

imc = peso / math.pow(alt, 2)

print(f"Seu IMC é, {imc:.1f}")




