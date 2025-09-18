lista = []
count = 0

while count<=9:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    count+=1
soma=sum(lista)
print("A soma de todos os números é",soma,"!")

media=soma/10
print("A média dos números é",media,"!")

"""Pedia um while que somasse 10 números inputados pelo usuário, fiz isso em forma de lista e incluí a média do resultado final"""