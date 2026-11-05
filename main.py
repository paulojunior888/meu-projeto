import datetime

print("--- BEM-VINDO AO PROGRAMA PYTHON ---")
nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem ou vai fazer este ano? "))

ano_atual = datetime.datetime.now().year
ano_nascimento = ano_atual - idade

print(f"\nOlá, {nome}! Você nasceu em {ano_nascimento}.")
