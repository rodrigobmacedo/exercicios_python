
#Exercício
#Peça ao usuário para digitar seu nome
#Peça ao usuário para digitar sua idade
#Se nome e idade forem digitados:
 #   Exiba:
  #      Seu nome é {nome}
   #     Seu nome invertido é {nome invertido}
    #    Seu nome contém (ou não) espaços
     #   Seu nome tem {n} letras
      #  A primeira letra do seu nome é {letra}
       # A última letra do seu nome é {letra}
#Se nada for digitado em nome ou idade: 
 #  exiba "Desculpe, você deixou campos vazios."
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome != "" and idade != "": 
    nome_invertido = nome[::-1 ] 
    print(f'Seu nome invertido: {nome_invertido}')
    if(' ' in nome):
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome contém {len(nome)} letras sendo a primeira: {nome[0]} e a última {nome[len(nome)-1]}')
else:
    print('Você deixou campos vazios')        