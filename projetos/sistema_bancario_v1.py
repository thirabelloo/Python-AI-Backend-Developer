SALDO = 0
NUMERO_SAQUES = 0
EXTRATO = ""
LIMITE_SAQUES = 3
SALDO_LIMITE_SAQUE = 500

def menu():
    """Exibe um menu com 4 opções e 
    retorna a opção escolhida pelo usuário.
    """
    
    print("""\n****** Seja bem vindo(a) ao Banco Gotham City!
    O maior Banco da Europa desde 1941 ****** """)
    print("\nSelecione uma operação:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair\n")


def depositar():
    global SALDO, EXTRATO
    valor = float(input("Informe o valor do depósito: "))
    if valor >= 1:
        SALDO += valor
        EXTRATO += f"Depósito R$: {valor:.2f} \n"
    else:
        print("Operação falhou! o valor informado é inválido.\n")


def sacar():
    global SALDO, NUMERO_SAQUES, LIMITE_SAQUES, EXTRATO
    if NUMERO_SAQUES >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
        return
    
    valor = float(input("Informe o valor que deseja sacar: "))
    if valor >= 1 and valor <= SALDO :
        if valor <= SALDO_LIMITE_SAQUE:
            SALDO -= valor 
            EXTRATO += f"Saque R$: {valor:.2f} \n"
            NUMERO_SAQUES += 1  
        else:
            print("Operação falhou! O valor do saque excede o limite.\n")   
    else:
        print("Operação falhou! Você não tem saldo suficiente.\n")


def extrato():
   print("\n========== EXTRATO =============")
   print("Não foram realizadas movimentações." if not EXTRATO else EXTRATO)
   print(f"Saldo R$:{SALDO}")
   print("=================================") 


def main():
     while True:
        opcao = int(input(menu()))
        if opcao == 1:
            depositar()
        elif opcao == 2:
            sacar()
        elif opcao == 3:
            extrato()
        elif opcao == 4:
            print("\nObrigado por ser nosso cliente, até breve.")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.\n")

main()