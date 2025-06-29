nome = 'Rodrigo Macedo'
tamanho_nome = len(nome)
contador = 0
nova_string = ''
int(contador)
while contador < tamanho_nome:
    nova_string += '*'
    nova_string += nome[contador]
    contador += 1
print(f'A String modificada ficou: {nova_string} ')    