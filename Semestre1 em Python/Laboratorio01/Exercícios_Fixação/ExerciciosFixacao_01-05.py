vogais=['a','e','i','o','u']

while True:
    letra=input("Digite a letra: ")

    if len(letra)!=1 or not letra.isalpha():
        print("Digite apenas uma letra!")
    else:
        break

if letra in vogais:
    print("A letra é uma vogal!")
else:
    print("A letra é uma consoante!")