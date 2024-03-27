def criarUsuario(usuarios):
    
    # Primeiro passo para a verificação de haver apenas um conta por cpf
    cpf = input("Seu Cpf (apenas numero): ")
    
    if cpf in usuarios:
        print('CPF já cadastrado')

    # Passando a primeira etapa agora vem o preenchimento das demais informações
    else:
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        endereço = input("longadouro, n° - bairro - cidade/sigla estado\n Rua Abc, 000 - Defg - hijk/Rj\n")
        
        # Criamos assim o cadastro do cliente ligado diretamente ao cpf
        novo_usuario = {cpf : [nome, data_nascimento, endereço]}
        return novo_usuario
    
def criarContaCorrente(numeroDaVez, usuarios):
    
    cpf = input("me informe seu cpf: ")
    
    #Aqui começa a verificação para ver se existe um usuário com esse cpf
    #Afim de não deixar uma conta sem usuário
    if cpf in usuarios:
        numero_da_conta = "0001 - " + str(numeroDaVez)
        print(f"Conta criada! Sua conta é: {numero_da_conta} ")
        return cpf, numero_da_conta
    
    #Caso não seja identificado a existência do usuário retorna o não registro do mesmo
    else:
        print("usuário não registrado")
        
def consulta(usuarios, contas):
    
    cpf = input("Informe seu cpf: ")
    
    #confere primeiramente a existência do mesmo   
    if cpf in usuarios:
        
        #já mostra todos os dados informados pelo usuário
        print(usuarios)
        
        # e aqui verifica dentre as contas criadas quais pertencem a esse cpf
        for conta in contas:
            if cpf in conta:
                print(conta)
    
    else:
        print("usuário não encontrado")
    
def validadorDeposito():
    
    # Valida a única condição de depósito que é de ser maior que 0
    if depositar_valor <= 0:
        print('Valor inválido')
        return False
    else:
        return True      

def depositar(valor_depositar, saldo):

    #Armazenará o histórico para fornecer dados ao Extrato
    historico_deposito = []
    
    #A ação de armazenar as informações importantes
    historico_deposito.append(f'Deposito: R${float(valor_depositar):.2f}')
    
    #Atualiza o saldo
    saldo += valor_depositar
    print("\n ### Depósito feito ### \n")
    
    return historico_deposito, saldo

def ValidadorSaque(saldo, valor_sacar, numero_de_saques):
    
    # Valida as condições para realizar o saque, nega o saque caso:
    # O valor a sacar é menor ou igual a zero, se tem saldo o suficiente e se já bateu o limite diário de valor de saques
    if valor_sacar <= 0 or valor_sacar > saldo or valor_sacar >500:
        print("saldo insuficiente ou Valor inválido")
        return False
    
    #e ainda valida para saber se bateu o limite diário de operações de saque
    elif numero_de_saques >= 3:
        print("Limite diário de saque atingido")
        return False
    
    else:
        return True

def sacar(valor_sacar, saldo):
    
    # Armazenará as informações para o extrato
    historico_sacado = []
    
    # Atualiza o saldo
    saldo -= valor_sacar
    
    # Armazena a tranferência
    historico_sacado.append(f'Saque: R${float(valor_sacar):.2f}')
                
    print('###Valor Sacado###')
    
    return historico_sacado, saldo

def extrato(historico, saldo):
    print('#### EXTRATO ####')
    
    # Aqui adiciona o saldo ao extrato
    historico.append(f'#### saldo final R${float(saldo):.2f} ####')
    
    # Mostra o extrato   
    print(*historico, sep='\n')
    
    # Após o extrato apaga o saldo afim de preparar para receber mais transições    
    historico.pop()
    
    return historico

    

import os

# O meunu afim de apresentar as opções de escolha
menu = '''
[D] Depósito
[S] Saque
[E] Extrato
[NU] Novo Usuário
[CC] Criar Conta Corrente
[C] Consultar contas
[Q] Sair
'''
#declara todas variáveis auxiliares e listas, dicionários para armazenamento

usuarios = {} # armazena as informações dos usuários no momento da criação

contas = [] # armazena as informações das contas no momento da criação  

numeroDaConta = 1 # número da conta corrente pós o 0001

contador_de_saque = 0 # certifica que a pessoa não irá passar o limite diário de 3 saques 

atualizacao = [] # serve para armazenar momentaneamente os dados da criação da conta

saldo = 0.00 # realiza operações de acordo com as opções escolhidas pelo usuário

historico = [] # armazena as operações para ser apresentado no extrato

while True:

  
    opcao = input(menu)
    os.system('cls')
    
    if opcao == "NU":
        try:
            
            #só faz com que a lista receba os novos usuários
            usuarios.update(criarUsuario(usuarios))
        
        except:
            continue
    
    if opcao == "CC":

        try:
            
            # armazena momentaneamente os dados na lista atualização
            atualizacao = list(criarContaCorrente(numeroDaVez=numeroDaConta, usuarios=usuarios))
            
            # atualiza para a próxima conta a ser criada
            numeroDaConta+=1
            
            # Aqui tira do armazenamento momentaneo para o definitivo
            contas.append(atualizacao)
        except:
            continue
 
    if opcao == "C":
        
        #Só realiza a consulta
        consulta(usuarios, contas) 
           
    if opcao == "D":
        
        print("\n### Área de Depósito ###\n")

        #recebe a informação do valor a ser depositado
        depositar_valor = float(input("Valor a ser depositado: R$ "))
        
        #aciona o validador
        if validadorDeposito():
            
            #armazena momentaneamente os dados
            deposito_historico_saldo = list(depositar(depositar_valor, saldo))
            
            #passa a primeira e a segunda informação as suas respectivas posições
            historico.append(*deposito_historico_saldo[0])
            saldo = deposito_historico_saldo[1]
            
        else:
            continue
                     
    elif opcao == "S":
        
        print("\n### Área de Saque ###\npermitido R$500,00 por saque\n")
        
        # recebe o valor que vai ser sacado
        sacar_valor = float(input("Valor a ser sacado: R$ "))
        
        # já ativa o validador
        if ValidadorSaque(saldo=saldo, valor_sacar=sacar_valor, numero_de_saques=contador_de_saque):
            
            # já atualiza a contagem de operações de saque
            contador_de_saque+=1

            # armazena momentaneamente as informações
            saque_historico_saldo = list(sacar(sacar_valor, saldo))
            
            # distribui respecitvamente as informações cedidas pelas funções
            historico.append(*saque_historico_saldo[0])
            saldo = saque_historico_saldo[1]
        else:
            continue
                     
    if opcao =="E":
        
        #puxa o histórico
        historico = extrato(historico,saldo = saldo)
        
    if opcao == "Q":
        #simplesmente quebra o código
        break
            
