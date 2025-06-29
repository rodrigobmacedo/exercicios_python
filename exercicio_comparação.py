primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')
if primeiro_valor > segundo_valor:
    print(f'O maior valor é: {primeiro_valor} ', f' O menor valor é: {segundo_valor} ')
elif primeiro_valor < segundo_valor:
    print(f'O maior valor é: {segundo_valor} ', f' O menor valor é: {primeiro_valor} ')
else:
    print("Os números são iguais")    