import time
tempo = 1.5

saldo = 0.00
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
menu = f"""
======= menu =======
Saldo: R${saldo: .2f}

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """


while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input(f"Informe o valor a ser depositado: "))
        saldo += valor
       
        
        print(f"Deposito no valor de {valor: .2f} realizado com sucesso")
        extrato += (f"+{valor: .2f} Deposito na conta.\n Saldo atual: R${saldo: .2f}.\n")
        
            
    elif opcao == "s":
        if LIMITE_SAQUES == 0:
            print("Você não tem mas saques disponivel. Volte amanhã para realizar novos saques.")
        
        if LIMITE_SAQUES > 0:
            
            print(f"Você tem {LIMITE_SAQUES} disponíveis")
            print(f"Lembrando que o limite de saque é de R$ {limite}")
            valor = float(input((f"Qual o valor a ser sacado? \n")))
            if valor <= limite and valor > 0 and valor <= saldo:
                LIMITE_SAQUES -= 1
                saldo -= valor
                print("sacando...")
                time.sleep(tempo)
                extrato += (f"-{valor:.2f}\tSaque na conta.\n Saldo atual: R${saldo: .2f}.\n")
                print(f"Saque no valor de R${valor: .2f} realizado com sucesso!")
            
            elif valor > limite:
                print("Não foi possível realizar o saque pois o valor desejado é maior que permitido\n")
            
            elif valor > saldo:
                print("Saldo insuficiente! Não será possível efetuar o saque!\n")

    elif opcao == "e":
        print("======== extrato ========\n")
        print(extrato)
        print("=========================")
        while True:
            visualizado = input("[1] Fechar\n=> ")
            if visualizado == "1":
                break
            else:
                print("\nComando Inválido, tente outra vez...\n=> ")
        
    elif opcao == "q":
        break
    
    else:
        print("Este comando é inválido. Escolha uma das opções do menu!")                    
    
    menu = f"""
======= menu =======
Saldo: R${saldo: .2f}

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """
    
                                                                                                                    
        
    