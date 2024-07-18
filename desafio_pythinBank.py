menu_opcoes = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo_conta = 0
limite_saque = 500
registro_extrato = ""
total_saques = 0
MAX_SAQUES = 3

def exibir_menu():
    return input(menu_opcoes)

def realizar_deposito(saldo, extrato):
    valor_deposito = float(input("Informe o valor do depósito: "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def realizar_saque(saldo, limite, extrato, saques):
    valor_saque = float(input("Informe o valor do saque: "))

    if valor_saque > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor_saque > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif saques >= MAX_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    escolha = exibir_menu()

    if escolha == "d":
        saldo_conta, registro_extrato = realizar_deposito(saldo_conta, registro_extrato)

    elif escolha == "s":
        saldo_conta, registro_extrato, total_saques = realizar_saque(saldo_conta, limite_saque, registro_extrato, total_saques)

    elif escolha == "e":
        exibir_extrato(saldo_conta, registro_extrato)

    elif escolha == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
