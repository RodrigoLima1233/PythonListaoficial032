'''
5) Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
'''

a = float(input("Indique um número:"))
b = float(input("Indique outro número:"))

# Operadores Aritiméticos
soma = a + b
sub = a - b
mult = a * b
div = a / b
div_inteiros = a // b


print(f"Soma desses números: { a + b }")
print(f"Subtração desses números: { a - b }")
print(f"Subtração do segundo número pelo primeiro: { b - a }")
print(f"Multiplicação desses números: { a * b }")
print(f"Divisão desses números: { a/b }")
print(f"Divisão de inteiros desses números: { a//b }")
print(f"Resto da divisão de por a: { a % b }")



