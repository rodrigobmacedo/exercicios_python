entrada = input("[E]ntrar [S]air")
senha = input("Senha: ")
senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print("Entrou")
elif entrada == 'S' or senha != senha_permitida:
    print("Saiu")
