from ..controller.leilao import Controller
import os

class View:
    def __init__(self):
        self.controller = Controller()
        self.leilao_iniciado = False

    def update_status(self):
        os.system('clear')
        print(self.controller.leilao.produto.nome)
        print('Preço inicial: ', self.controller.leilao.produto.preco_inicial)
        print('Vendedor: ', self.controller.leilao.vendedor.nome)
        print('Maior lance: ', self.controller.maior_lance)


    def vendedor_fluxo(self):
        if not self.leilao_iniciado:
            v = int(input("0-Sair\n1-Criar leilao"))
            if v == 1:
                nome_vendedor = input('Digite seu nome: ')
                nome_produto = input('Digite o nome do produto: ')
                preco_produto = float(input('Digite o preço inicial do produto: '))

                self.controller.cria_leilao(nome_vendedor, nome_produto, preco_produto)
                self.leilao_iniciado = True
                self.update_status()
        else:
            v = int(input("0-Sair\n1-Encerrar leilão"))
            if v == 1:
                self.controller.encerra_leilao()
                self.leilao_iniciado = False



    def comprador_fluxo(self):
        v = -1
        while v != 0:
            v = int(input("0-Sair\n1-Dar lance\n"))
            if v == 1:
                for k, v in self.controller.leilao.lances.items():
                    print(k, ': ', v)

                nome_comprador = input('Digite seu nome: ')
                preco = float(input('Digite o valor: '))
                self.controller.cria_lance(nome_comprador, preco)
                self.update_status()

    def main(self):
        v = -1
        while v != 0:
            v = int(input("0-Sair\n1-Vendedor\n2-Comprador\n"))
            if v == 1:
                self.vendedor_fluxo()
            elif v == 2:
                self.comprador_fluxo()
