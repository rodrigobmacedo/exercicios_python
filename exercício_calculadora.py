resultado = 0
n1 = 0
n2 = 0
saida = False
opcao = ''
while saida == False:        
        opcao = input("Escolha o que fazer da sua vida\n D para dividir \n S para somar \n M para multiplicar \n T para subtrair \n E para sair do programa\n:")
        opcao = opcao.upper()
        if opcao != 'D' and opcao != 'S' and opcao != 'M' and opcao != 'T' and opcao != 'E':
             print("Você digitou uma operação inválida")
        elif opcao == 'E':
            print("Saindo do programa....")
            break
        else:
            try:         
                n1 = float(input("\nDigite o primeiro número: "))
                n2 = float(input("\nDigite o segundo número: "))    
                if opcao == 'D':
                    resultado = n1/n2
                elif opcao == 'S':
                    resultado = n1+n2
                elif opcao == 'M':
                    resultado = n1*n2
                elif opcao == 'T':
                    resultado = n1-n2
            except:
                 print("Um dos números digitados não é valido!")
                                  
        print(f"\n\nO resultado é: {resultado}")     
    
  
        



     
