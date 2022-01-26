class Funcionario:

    def __init__(self, nome, funcao, salario=1400):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

    def mostrar(self):
        print(f"Nome: {self.nome}\n"
              f"Função: {self.funcao}\n"
              f"Salário: {self.salario}")

    def aumentar_salario(self):
        while True:
            try:
                porcentual = float(input("Quanto porcento deseja aumentar? "))
            except(TypeError, ValueError):
                print("Por favor, digite uma porcentagem válida")
            else:
                break
        print(f"Salário de {self.nome} aumentado em {porcentual}%!")
        self.salario += (self.salario * porcentual / 100)
        print(f"O salário de {self.nome} agora é {self.salario}")
        return


print("Bem vindo ao sistema gerenciador de funcionários")
maria = Funcionario('Maria', 'Médica', 20000)
joao = Funcionario('João', 'Zelador')
jose = Funcionario('José', 'Enfermeiro', 5000)
diana = Funcionario('Diana', 'Motorista', 2000)

print()

while True:
    print("O que deseja fazer?\n[1] Mostrar funcionários\n[2] Aumentar salário\n[3] Sair do programa")
    opcao = input("Sua opção: ")

    if opcao == '1':
        maria.mostrar()
        print()
        joao.mostrar()
        print()
        jose.mostrar()
        print()
        diana.mostrar()

    elif opcao == '2':
        while True:
            opcao2 = input("De quem deseja aumentar o salário? ").lower()
            if opcao2 == 'maria':
                maria.aumentar_salario()
                break
            elif opcao2 == 'joão':
                joao.aumentar_salario()
                break
            elif opcao2 == 'josé':
                jose.aumentar_salario()
                break
            elif opcao2 == 'diana':
                diana.aumentar_salario()
                break
            else:
                print("Por favor, digite um funcionário existente!")
                continue

    elif opcao == '3':
        break

print("Obrigado por usar nosso programa!")
