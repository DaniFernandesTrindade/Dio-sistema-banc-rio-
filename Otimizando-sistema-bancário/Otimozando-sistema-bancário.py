# Funções do sistema
def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, extrato, valor, limite, saques_realizados, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print(f"Valor excede o limite de R$ {limite:.2f} por saque.")
    elif saques_realizados >= limite_saques:
        print("Limite de saques diários atingido.")
    elif valor <= 0:
        print("Valor inválido para saque.")
    else:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        saques_realizados += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, saques_realizados

def exibir_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("===================\n")

# Inicialização de variáveis
saldo = 0.0
extrato = []
limite = 500
saques_realizados = 0
LIMITE_SAQUES = 3

# Menu principal
while True:
    print("""
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
    """)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, extrato, valor)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, saques_realizados = sacar(saldo, extrato, valor, limite, saques_realizados, LIMITE_SAQUES)

    elif opcao == "3":
        exibir_extrato(saldo, extrato)

    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema bancário!")
        break

    else:
        print("Opção inválida. Tente novamente.")
