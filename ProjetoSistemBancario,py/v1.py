def depositar(valor_depositar):
    #cria-se uma lista para armazenar a str abaixo
    historico_deposito = []
    
    #str que se armazena na lista "historico_deposito"
    historico_deposito.append(f'Deposito: R${float(valor_depositar):.2f}')

    print("\n ### Depósito feito ### \n")
    
    #retorna a lista para poder transferir os dados recebidos para o extrato
    return historico_deposito


def sacar(valor_sacar):
    #cria-se uma lista para armazenar a str abaixo
    historico_sacado = []
    
    #str que se armazena na lista "historico_sacado" 
    historico_sacado.append(f'Saque: R${float(valor_sacar):.2f}')
                
    print('###Valor Sacado###')
    
    #retorna a lista para poder transferir os dados recebidos para o extrato
    return historico_sacado
    
#para conseguir usar a função "cls" para limpar o terminal
import os

#definimos aqui uma variável com as opções do menu
menu = '''
[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair
'''

#cria-se uma variável para armazenar quantas vezes foram feitos os saques
contador_de_saque = 0
#cria-se uma váriavel para o saldo
saldo = 0.00
#histórico de transações para o extrato
historico = []

#mantém em ciclo
while True:

    #recebe-se do usuário a operação desejada
    opcao = input(menu)
    #limpa o terminal
    os.system('cls')
    
    #agoras as condições da escolha do usuário
    
    if opcao == "D":
        
        print("\n### Área de Depósito ###\n")

        #recebe a resposta ja convertida em flutuante (float)
        depositar_valor = float(input("Valor a ser depositado: R$ "))

        #verifica a condição de ser positivo para realizar o depósito
        if depositar_valor <= 0:
            print('Valor inválido')
            continue
        
        #etapa de realização do depósito
        else:
            #atualização de saldo
            saldo += depositar_valor
            
            #atualização do extrato através da função "depositar"
            #o "*" serve para desempacotar as informações 
            historico.append(*depositar(depositar_valor))
            
            
    elif opcao == "S":
        
        print("\n### Área de Saque ###\npermitido R$500,00 por saque\n")
        
        #recebe a resposta ja convertida em flutuante (float)
        sacar_valor = float(input("Valor a ser sacado: R$ "))
        
        #verifica as condições para que o saque seja feito
        if sacar_valor <= 0 or sacar_valor > saldo or sacar_valor > 500:
            print("Saldo Insuficiente ou Valor inválido")
            continue
        
        #aprovado nas condições aqui é realizada a última verificação
        else:        
            #verificação de quantidade de operações de saque   
            if contador_de_saque >=3:
                print('Limite de saque diário atingido!')
                continue
            
            #realização do saque
            else:
                #alteração do saldo
                saldo -= sacar_valor
                
                #contador da operação
                contador_de_saque+=1

                #atualização do extrato através da função "depositar"
                #o "*" serve para desempacotar as informações 
                historico.append(*sacar(sacar_valor))
                
                
    if opcao =="E":
        print('#### EXTRATO ####')
        
        #Adiciona-se o saldo final ao extrato
        historico.append(f'#### saldo final R${float(saldo):.2f} ####')
       
        #amostra o extrato já com "*" para desempacotar as informações
        #separados "sep" ja pela quebra de linha "\n"
        print(*historico, sep='\n')
        
        #apago o dado do saldo final do extrato, para caso haja mais
        #transições não conste o extrato antigo
        historico.pop()
        
    if opcao == "Q":
        #simplesmente quebra o código
        break
            
