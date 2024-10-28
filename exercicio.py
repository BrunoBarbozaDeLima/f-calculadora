def calculadora():
    while True:
        print("\nEscolha a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        # Solicita a operação
        opcao = input("Digite o número da operação: ")

        # Opção de sair
        if opcao == '0':
            print("Encerrando a calculadora. Até mais!")
            break

        # Valida a operação escolhida
        if opcao not in ['1', '2', '3', '4']:
            print("Essa opção não existe.")
            continue

        # Solicita os números para a operação
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

        # Realiza a operação e exibe o resultado
        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado da Soma: {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado da Subtração: {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado da Multiplicação: {resultado}")
        elif opcao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da Divisão: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        
# Executa a calculadora
calculadora()
