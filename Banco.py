class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente para realizar o saque.')

    def extrato(self):
        print(f'\nExtrato bancário de {self.titular}:')
        print(f'Saldo atual: R${self.saldo:.2f}')

# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma conta bancária
    minha_conta = ContaBancaria("João")

    # Fazendo operações
    minha_conta.deposito(100.00)
    minha_conta.saque(50.00)
    minha_conta.extrato()

    minha_conta.saque(70.00)  # Tentando sacar mais do que o saldo
    minha_conta.extrato()

    minha_conta.deposito(150.00)
    minha_conta.extrato()
