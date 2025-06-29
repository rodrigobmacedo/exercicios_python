numero = input("Digite um número inteiro: ")
numero = float(numero)
if numero % 2 == 0 and numero.is_integer():
    print(f"o número {numero} é PAR e é inteiro")
elif numero % 2 != 0 and numero.is_integer():
    print(f"o número {numero} não é PAR mas é inteiro")
elif not numero.is_integer():
    print(f"o número {numero} não é inteiro")
