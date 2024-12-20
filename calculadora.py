def calculadora():
    memoria = [0]

    while True:
        print("Escolha uma operação:")
        print("1 = Soma")
        print("2 = Subtração")
        print("3 = Multiplicação")
        print("4 = Divisão")
        print("5 = Memória")
        print("6 = Sair")

        operacao = int(input("Insira o número da operação: "))
        
        if operacao == 6:
            print("Saindo da calculadora")
            break

        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))

        if operacao == 5:
          print (memoria)

        elif operacao == 1:
                resultado = num1 + num2
                print(f"O resultado da soma é: {resultado}")
                memoria.append (resultado)

        elif operacao == 2:
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
                memoria.append(resultado)
        elif operacao == 3:
                resultado = num1 * num2
                print(f"O resultado da multiplicação é: {resultado}")
                memoria.append(resultado)
        elif operacao == 4:
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"O resultado da divisão é: {resultado}")
                    memoria.append(resultado)
                else:
                    print("Erro: Não é possível dividir por zero.")
                    print("")
                    continue
    
calculadora()