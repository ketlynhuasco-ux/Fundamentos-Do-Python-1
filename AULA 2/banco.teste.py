saldo = 5000.20
senha = 1234

print('Banco Z...')
print('seja bem vindo(a)')
senha = int(input('digite sua senha: '))
op = input('''
escolha a operação:
1 - Saque
2 - Deposito
3 - Extrato
''')
resultado = op == '1' and float(input('Voce escolheu saque R$: ')) -saldo or op == '2' and float(input('Voce escolheu Deposito')) + saldo or ('Extrato:', saldo)
print(resultado)
