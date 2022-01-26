"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e
mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e
mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
"""
from pprint import pprint


class BombaCombustivel:

    def __init__(self, tipo='gasolina', valor=5.0, quantidade=300.0):
        self.tipo = tipo
        self.valor = valor
        self.quantidade = quantidade

    def abastecer_por_valor(self):
        while True:
            try:
                valor_abastecimento = float(input("Quanto deseja abastecer em reais? R$"))
            except(ValueError, TypeError):
                print("Por favor, digite um número!")
            else:
                break

        abastecimento = valor_abastecimento / self.valor
        self.quantidade -= abastecimento
        print(f"Serão abastecidos {abastecimento:.2f} litros de combustível")
        print(f"A bomba agora tem {self.quantidade:.2f} litros")

    def abastecer_por_litro(self):
        while True:
            try:
                quantidade_abastecimento = float(input("Quantos litros deseja abastecer?"))
            except(ValueError, TypeError):
                print("Por favor, digite um número")
            else:
                break

        preco = quantidade_abastecimento * self.valor
        self.quantidade -= quantidade_abastecimento
        print(f"O abastecimento custará R${preco:.2f}")
        print(f"A bomba agora tem {self.quantidade:.2f} litros")

    def alterar_valor(self):
        while True:
            try:
                novo_valor = float(input("Qual será o novo valor do combustível? R$"))
            except(ValueError, TypeError):
                print("Por favor, digite um número. ")
            else:
                break

        self.valor = novo_valor
        print(f"O novo valor do combustível R${self.valor:.2f}")

    def alterar_combustivel(self):
        novo_tipo = str(input("Qual será o novo combustível? "))
        self.tipo = novo_tipo
        print(f"O novo combustível será {self.tipo}")

    def alterar_quantidade(self):
        print('Deseja adicionar ou remover combustível da bomba? ')
        while True:

            try:
                opcao = input("Sua opcao: ").strip().lower()
                quantidade = float(input('Quantos litros deseja alterar? '))

            except(TypeError, ValueError):
                print("Por favor, digite opção válida. Você digitou um número em quantidade?")
                continue

            if not 'adicionar' or 'remover' in opcao:
                continue
            else:
                break

        if 'adicionar' in opcao:
            self.quantidade += quantidade
        else:
            self.quantidade -= quantidade
        print(f"A Bomba agora tem {self.quantidade:.2f} litros")


print("Bem vindo ao programa da bomba de combustível")

tipo = str(input("Qual será o tipo de combustível? ."))
valor = float(input("Qual será o valor do combustível? R$"))
quantidade = float(input("Qual será a quantidade de combustível inicial? "))

bomba = BombaCombustivel(tipo, valor, quantidade)

while True:
    print()
    print("[1] Abastecer por valor\n[2] Abastecer por litro\n[3] Alterar Combustível\n[4] Alterar quantidade\n"
          "[5] Alterar valor\n[6] Mostrar dados da bomba\n[7] Sair")
    print()
    opcao = str(input("Sua opção: "))

    if opcao == '1':
        bomba.abastecer_por_valor()
        continue
    elif opcao == '2':
        bomba.abastecer_por_litro()
        continue
    elif opcao == '3':
        bomba.alterar_combustivel()
        continue
    elif opcao == '4':
        bomba.alterar_quantidade()
        continue
    elif opcao == '5':
        bomba.alterar_valor()
        continue
    elif opcao == '6':
        print(f"O tipo de combustível é {bomba.tipo} ")

    elif opcao == '7':
        break
    else:
        print("Por favor, escolha uma opção válida! ")
        continue
