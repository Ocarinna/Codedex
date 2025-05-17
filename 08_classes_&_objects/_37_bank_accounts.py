#It's time to open up a bank account! 🏦

#Create a file called bank_accounts.py.

#Let's define a BankAccount class. Then, let's use the __init__() method to set the following attributes:

#first_name (string)
#last_name (string)
#account_id (integer)
#account_type (string)
#pin (integer)
#balance (float)
#Next, let's create three methods:

#.deposit(): Add money into the account and return the new balance.
#.withdraw(): Take money out by subtracting from balance and returning the withdrawn amount.
#.display_balance(): Print the current value of balance.
#Lastly, initialize a new object from the BankAccount class and use these methods to do the following:

#Deposit $96 in the account.
#Withdraw $25 from the account.
#Print the current account balance.

print("Bem-vindo ao Banco FROMT!")

class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = float(balance)
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Depósito de R${amount} realizado com sucesso!")
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Saldo insuficiente!")
            return 0
        self.balance -= amount
        print(f"Saque de R${amount} realizado com sucesso!")
        return amount
    
    def display_balance(self):
        print(f"\n=== Extrato Bancário ===")
        print(f"Cliente: {self.first_name} {self.last_name}")
        print(f"Conta: {self.account_id} - Tipo: {self.account_type}")
        print(f"Saldo atual: R${self.balance:.2f}\n")

print("Para criar sua conta, forneça os dados solicitados:")
cliente_1 = BankAccount(
    first_name=input("Qual seu nome?\n"),
    last_name=input("Qual seu sobrenome?\n"),
    account_id=int(input("Qual código de conta?\n")),
    account_type=input("Qual o tipo da sua conta?\n"),
    pin=int(input("Qual a senha da sua conta?\n")),
    balance=float(input("Quanto tem em sua conta?\n")),
)

while True:
    print("\nEscolha a operação desejada:")
    print("(1) Depositar")
    print("(2) Sacar")
    print("(3) Ver Saldo")
    print("(4) Sair")
    
    opcao = input("Digite o número da operação: ")
    
    if opcao == '1':
        valor = float(input("Quanto deseja depositar? R$"))
        cliente_1.deposit(valor)
    elif opcao == '2':
        valor = float(input("Quanto deseja sacar? R$"))
        cliente_1.withdraw(valor)
    elif opcao == '3':
        cliente_1.display_balance()
    elif opcao == '4':
        print("Obrigado por usar nossos serviços!")
        break
    else:
        print("Opção inválida! Tente novamente.")