menu = """

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair
[i] Empréstimo

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
emprestimo = ""
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo_excedido = valor > saldo

        limite_excedido = valor > limite

        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif limite_excedido:
            print("Saldo insuficiente! O valor do saque excede o limite.")

        elif saque_excedido:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não houve nenhuma  movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "i":
        valor= float(input("Informe o valor do empréstimo!!"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Empréstimo: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

            
    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada.")
