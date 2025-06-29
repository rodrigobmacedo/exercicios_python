tentativas = 5
palavra = input("Digite a palavra para secreta")
palavra_secreta = palavra.upper()
palavra_escondida = "_"*len(palavra_secreta)
lista_palavra = list(palavra_escondida)
tamanho_palavra = len(palavra_secreta)
letras_digitadas = ""
cont_acerto = 0;
i = 0
ganhou = False
print("\n\n INICIANDO O JOGO! \n\n")
while tentativas != 0 and ganhou == False:
    cont_acerto = 0
    cont_repetida = 0
    lista_palavra = list(lista_palavra)
    letra = input("\nDigite uma letra para procurar: ")
    if letra in letras_digitadas:
        print("Esta letra ja foi digitada")
        cont_repetida = 1
    else:    
        letras_digitadas += letra+"-"
        letra_procurada = letra.upper()
        for i in range(tamanho_palavra):
            if letra_procurada == palavra_secreta[i]:
                lista_palavra[i] = letra_procurada
                cont_acerto = 1
            elif letra_procurada != [i] and cont_acerto == 0:
                cont_acerto = 0
            if "_" not in lista_palavra :
                lista_palavra = "".join(lista_palavra)
                print(f"PARABÉNS, VOCÊ VENCEU\na palavra secreta era: {lista_palavra}")
                ganhou = True   
    if cont_acerto == 0 and cont_repetida != 1:
        tentativas -= 1        
        print("\nVOCÊ ERROU A LETRA\n")
    lista_palavra = "".join(lista_palavra)
    if ganhou == False and tentativas >0:
        print(f"VOCÊ AINDA TEM {tentativas} CHANCES\n{lista_palavra}")
        print(letras_digitadas)
    if tentativas == 0:
        print(f"VOCÊ PERDEU\nA palavra secreta era {palavra_secreta}")   