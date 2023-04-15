# Função para adição
def soma(a, b):
    return a + b

# Função para subtração
def subtracao(a, b):
    return a - b

# Função para multiplicação
def multiplicacao(a, b):
    return a * b

# Função para divisão
def divisao(a, b):
    if b == 0:
        print("Erro: divisão por zero!")
        return None
    else:
        return a / b
    
#Funão de porcentagem
def porcentagem(a, b):
    if b == 0:
        print("Erro: porcentagem por zero!")
        return None
    else:
        return (a * b) / 100

# Função principal
def calculadora():
    while True:
        print("Escolha uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Porcentagem")
        print("6. Sair")
        opcao = input("Digite o número da operação que você deseja (1/2/3/4/5/6): ")

        if opcao == '6':
            print("Encerrando a calculadora...")
            break

        if opcao not in ['1', '2', '3', '4', '5']:
            print("Opção inválida. Tente novamente.")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            resultado = soma(num1, num2)
            print("Resultado é: ", resultado)
        elif opcao == '2':
            resultado = subtracao(num1, num2)
            print("Resultado é: ", resultado)
        elif opcao == '3':
            resultado = multiplicacao(num1, num2)
            print("Resultado é: ", resultado)
        elif opcao == '4':
            resultado = divisao(num1, num2)
            if resultado is not None:
                print("Resultado é: ", resultado)
        elif opcao == '5':
            resultado = porcentagem(num1, num2)
            if resultado is not None:
                print("Resultado é: ", resultado)

# Chamada da função principal
calculadora()
