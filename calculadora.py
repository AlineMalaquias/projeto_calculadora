def calculadora():
    memoria = [0]

    while True:
        print("Escolha uma operação:")
        print("1 = Soma")
        print("2 = Subtração")
        print("3 = Multiplicação")
        print("4 = Divisão")
        print("5 = Sair")

        operacao = int(input("Insira o número da operação: "))
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))

        if operacao == 5:
            print("Saindo da calculadora")
            break

        if operacao == 1:
            resultado = num1 + num2
            memoria[0] = resultado
            print(f"O resultado da soma é: {resultado}")
        elif operacao == 2:
            resultado = num1 - num2
            memoria[0] = resultado
            print(f"O resultado da subtração é: {resultado}")
        elif operacao == 3:
            resultado = num1 * num2
            memoria[0] = resultado
            print(f"O resultado da multiplicação é: {resultado}")
        elif operacao == 4:
            if num2 != 0:
                resultado = num1 / num2
                memoria[0] = resultado
                print(f"O resultado da divisão é: {resultado}")
            else:
                print("Erro: Não é possível dividir por zero.")
                print("")
        
        print(memoria.append(operacao))  
        print(memoria[0])
        continue

calculadora()