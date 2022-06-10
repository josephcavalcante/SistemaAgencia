
print('olá, bem vindo ao caixa')
while True:
    agencia=input('insira a agencia')
    if (agencia=='1100-0'):
        print('agencia aceita!')
        break
    else:
        print('agencia invalida')
        continue 
while True:
    conta=input('insira a conta')
    if (conta=='11111-0'):
        print('conta aceita!')
        break
    else:
        print('conta recusada')
        continue
while True:
    senha=input('insira sua senha')
    if (senha=='123456'):
        print('senha aceita!')
        break
    else:
        print('senha recusada')
        continue
    

if(senha=='123456'):
        print('login aceito')
saldo1=0
saldo2=0
while True:
    print('-----------------------------')
    print('⠀⠀⠀⠀⠀⠀⠀menu principal')
    print('-----------------------------')

    print('1:Depósito na conta corrente')
    print('2:Depósito na conta poupança')
    print('3:Saque da conta corrente')
    print('4:Saque da poupança')
    print('5:Saldo da conta corrente')
    print('6:Saldo da poupança')
    print('7:Transferência da conta corrente para poupança')
    print('8:Transferência da conta poupança para corrente')
    print('9:sair')
    print('-----------------------------')
    operação=input('que operação deseja fazer?:')
    if (operação=='9'):
        break
    senha=input('insira sua senha')
    while senha!='123456':
        senha=input('senha incorreta')
    if (operação=='1'):
        valor_deposito=int(input('valor do deposito?:'))
        saldo1= saldo1 + valor_deposito
        print('operação efetuada!')

    if (operação=='2'):
        valor_deposito2=int(input('valor do deposito?:'))
        saldo2=saldo2+valor_deposito2
        print('operação efetuada!')

    if (operação=='3'):
        valor_saque=int(input('valor do saque?:'))
        while valor_saque>saldo1:
            valor_saque=int(input('valor de saque invalido'))
        saldo1=saldo1-valor_saque
        print('operação efetuada!')

    if (operação=='4'):
        valor_saque2=int(input('valor do saque?:'))
        while valor_saque2>saldo2:
            valor_saque2=int=input('valor de saque invalido')
        saldo2=saldo2-valor_saque
        print('operação efetuada!')
    if (operação=='5'):
        print(saldo1)
        print('operação efetuada!')

    if (operação=='6'):
        print(saldo2)
        print('operação efetuada!')

    if (operação=='7'):
        valor_transferencia=int(input('insira o valor da tranferencia'))
        while valor_transferencia>saldo1:
            valor_transferencia=int(input('transferencia invalida'))
        saldo1=(saldo1-valor_transferencia)
        saldo2=(saldo2+valor_transferencia)
        print('operação efetuada!')
    if (operação=='8'):
        valor_transferencia=int(input('insira o valor da tranferencia'))
        while valor_transferencia>saldo2:
            valor_transferencia=int(input('transferencia invalida'))
        saldo2=(saldo2-valor_transferencia)
        saldo1=(saldo1+valor_transferencia)
        print('operação efetuada!')
    
   
        



        










           
