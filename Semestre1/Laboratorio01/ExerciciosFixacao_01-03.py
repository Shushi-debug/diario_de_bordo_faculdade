import calendar

ano=int(input("Digite o nome do ano para verificar se é bissexto: "))

def verificarAnoBissexto (ano):
    return calendar.isleap(ano)

if verificarAnoBissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto :(")


"""Exercício para verificar se o ano é bissexto, poderia ter sido feito pela divisão de 4, mas preferi procurar uma outra forma de implementar e existe uma biblioteca para calendar, achei dahora! :D"""
