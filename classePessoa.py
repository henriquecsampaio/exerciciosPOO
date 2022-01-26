"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        for ano in range(anos):
            while self.idade < 21:
                self.altura += 0.5
            self.idade += 1
        print(f"A idade de {self.nome} agora é {self.idade} anos")

    def engordar(self, kilos):
        self.peso += kilos
        print(f"O peso de {self.nome} agora é {self.peso} kilos")

    def emagrecer(self, kilos):
        self.peso -= kilos
        print(f"O peso de {self.nome} agora é {self.peso} kilos")

    def crescer(self, centimetros):
        self.altura += centimetros
        print(f"A altura de {self.nome} agora é {self.altura}cm")


p1 = Pessoa('Henrique', 20, 80, 178)
p1.envelhecer(1)
p1.engordar(3)
p1.emagrecer(7)
p1.crescer(3)
