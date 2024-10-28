# f-calculadora
 função calculadora 

 # Calculadora em Python

Este projeto é uma calculadora simples em Python que permite ao usuário realizar operações matemáticas básicas. A calculadora continua funcionando em um loop infinito até que o usuário escolha a opção de sair. 

## Funcionalidades

O programa permite ao usuário realizar as seguintes operações:
1. **Soma**
2. **Subtração**
3. **Multiplicação**
4. **Divisão**

Além disso, o programa:
- Exibe uma mensagem de erro se o usuário escolher uma opção inválida.
- Trata a divisão por zero, informando ao usuário que não é possível dividir por zero.
- Finaliza apenas quando o usuário escolhe explicitamente a opção de sair.

## Estrutura do Código

O código consiste em uma única função `calculadora()`, que executa todo o processo de interação com o usuário.

### Passo a Passo

1. **Exibição do Menu de Opções**:
   - O programa exibe as opções de operação para o usuário. Este menu é mostrado repetidamente a cada nova operação ou caso o usuário escolha uma opção inválida.

2. **Leitura da Opção do Usuário**:
   - O programa lê a opção digitada pelo usuário e verifica se é válida.
   - Se a opção for `'0'`, o programa exibe uma mensagem de despedida e encerra.
   - Se a opção não for reconhecida (não está entre `'0'`, `'1'`, `'2'`, `'3'`, ou `'4'`), o programa exibe a mensagem “Essa opção não existe” e volta ao menu de opções.

3. **Leitura dos Números**:
   - Caso o usuário escolha uma operação válida, o programa solicita dois números para realizar a operação.
   - O programa trata possíveis erros de entrada, como quando o usuário digita algo que não é um número, e solicita a entrada novamente.

4. **Execução da Operação e Exibição do Resultado**:
   - O programa realiza a operação escolhida:
     - **Soma** (`opcao == '1'`): Soma os dois números e exibe o resultado.
     - **Subtração** (`opcao == '2'`): Subtrai o segundo número do primeiro e exibe o resultado.
     - **Multiplicação** (`opcao == '3'`): Multiplica os dois números e exibe o resultado.
     - **Divisão** (`opcao == '4'`): Divide o primeiro número pelo segundo e exibe o resultado, a menos que o segundo número seja zero, caso em que exibe uma mensagem de erro.
   - Após exibir o resultado, o programa volta ao menu de opções.

### Exemplo de Uso

```plaintext
Escolha a operação:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair
Digite o número da operação: 1
Digite o primeiro número: 5
Digite o segundo número: 3
Resultado da Soma: 8.0

