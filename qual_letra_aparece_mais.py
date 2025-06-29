palavra = input("Digite uma frase: ")
tamanho = int(len(palavra))
i = 0
contador_letra = 0
letra = ''
quantidade = 0


while i < tamanho:
    quantidade = palavra.count(palavra[i])
    if quantidade > contador_letra:
        contador_letra = quantidade
        letra = palavra[i]



    i += 1    

print(f"A letra {letra} apareceu {contador_letra} vezes")    

