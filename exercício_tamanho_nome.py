nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)
try:
    if tamanho_nome <= 4:
        print("Teu nome é curto!")
    elif tamanho_nome > 4 and tamanho_nome <= 6:
        print("Teu nome é normal!")
    elif(tamanho_nome > 6):
        print("Teu nome é muito grande")
except:
    print("ERRO!")                