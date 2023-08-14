'''
6) Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
'''

nome = input("Olá, qual é o seu nome?")
sal = input("E qual é o seu salário?")
total = float(input("E qual é o total de vendas?"))

comi = total + total /15
comissao = input(f"Informe sua comissão: {comi}")

salc = sal + comi

print(f"Então o seu nome é {nome} ")
print(f"Seu salário é {sal}")
print(f"Sua comissão é {comissao}")
print(f"Seu salário completo é {salc}")



