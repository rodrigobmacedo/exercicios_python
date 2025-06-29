nome = 'Rodrigo'
#print(nome[2])
#print('a' in nome) # vai dizer se a letra a está na string nome
encontrar = input("Digite uma letra para encontrar: ")
if encontrar in nome:
    print(f'a letra {encontrar} está em {nome}' )
else:
    print(f'a letra {encontrar} não está em {nome}')
    