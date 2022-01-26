"""
Crie uma classe que modele um Tamaguchi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamaguchi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""


class Tamaguchi:

    def __init__(self, nome, idade=1, alimentacao=100, saude=100):
        self.nome = nome
        self.alimentacao = alimentacao
        self.saude = saude
        self.idade = idade

    def alterar_nome(self):
        novo_nome = str(input("Qual nome deseja colocar em seu Tamaguchi? "))
        self.nome = novo_nome
        print(f"O novo nome do seu bichinho é {self.nome}!")

    def alterar_idade(self):
        nova_idade = int(input("Quantos anos deseja adicionar ao seu bichinho? "))
        self.idade += nova_idade
        print(f"O seu bichinho agora tem {self.idade} anos!")

    def alterar_saude(self):
        opcao = str(input("Você deseja aumentar ou diminuir a saúde do seu Tamaguchi? ")).strip().lower()
        if 'diminuir' in opcao:
            reducao = float(input("Quanto deseja diminuir em %? "))
            self.saude -= reducao
        if 'aumentar' in opcao:
            soma = float(input("Quanto deseja somar em %? "))
            self.saude += soma
        print(f"A saúde do seu bicinho está em {self.saude}%")

    def alterar_alimentacao(self):
        opcao = str(input("Você deseja aumentar ou diminuir a alimentação do seu Tamaguchi? ")).strip().lower()
        if 'diminuir' in opcao:
            reducao = float(input("Quanto deseja diminuir em %? "))
            self.alimentacao -= reducao
        if 'aumentar' in opcao:
            soma = float(input("Quanto deseja somar em %? "))
            self.alimentacao += soma
        print(f"A alimentação do seu bichinho está em {self.alimentacao}%")

    def mostrar_humor(self):
        humor = (self.saude + self.alimentacao) / 2
        print(f"O humor do seu Tamaguchi está em {humor}%")


# Programa
print("Bem vindo ao seu Tamaguchi!")
print()
print("Primeiro, vamos criar seu bichinho!")

nome = str(input("Nome: "))
idade = int(input("Idade: "))
bichinho = Tamaguchi(nome, idade)

print()
print(f"Parabéns! O nome do seu tamaguchi é {bichinho.nome} e ele tem {bichinho.idade} anos!")

while True:
    print()
    print("O que deseja fazer?\n[1] Alterar nome\n[2] Alterar idade\n[3] Alterar alimentação\n[4] Alterar saúde\n"
          "[5] Verificar humor\n[6] Sair")
    opcao = str(input("Sua opção: "))
    if opcao == '1':
        bichinho.alterar_nome()
    if opcao == '2':
        bichinho.alterar_idade()
    if opcao == '3':
        bichinho.alterar_alimentacao()
    if opcao == '4':
        bichinho.alterar_saude()
    if opcao == '5':
        bichinho.mostrar_humor()
    if opcao == '6':
        break

print()
print("Obrigado por brincar conosco! Até a próxima!")
