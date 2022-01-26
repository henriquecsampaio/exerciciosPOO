"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""


class TV:

    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print(f"A tv agora está no canal {self.canal}")
        else:
            print(f"Canal inválido! Por favor tente um entre 0 e 100.")

    def aumentar_volume(self, aumento):
        if self.volume + aumento <= 100:
            self.volume += aumento
            print(f"A TV agora está no volume {self.volume} ")
        else:
            print(f"Erro! O volume deve ficar entre 0 e 100!")

    def diminuir_volume(self, reducao):
        if self.volume - reducao >= 0:
            self.volume -= reducao
            print(f"A TV agora está no volume {self.volume}")
        else:
            print(f"Erro! O volume deve ficar entre 0 e 100!")


print("Bem vindo à sua TV!")
print()
televisao = TV(1, 50)

while True:

    print("O que deseja fazer?\n[1] Mudar o canal\n[2] Aumentar volume\n[3] Diminuir volume\n[4] Sair")

    while True:
        opcao = str(input("Sua opção: "))
        if opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4':
            break
        else:
            continue

    if opcao == '1':
        while True:
            try:
                novo_canal = int(input("Qual canal deseja acessar? "))
            except(ValueError, TypeError):
                print("Por favor, digite um valor válido")
                continue
            else:
                break
        televisao.mudar_canal(novo_canal)

    if opcao == '2':
        aumento = int(input("Quanto de volume deseja aumentar? "))
        televisao.aumentar_volume(aumento)

    if opcao == '3':
        reducao = int(input("Quanto de volume deseja reduzir? "))
        televisao.diminuir_volume(reducao)

    if opcao == '4':
        break

print("Obrigado por usar nossa televisão!")
