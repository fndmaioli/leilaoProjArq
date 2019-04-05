from ..model.leilao import Leilao
from ..model.lance import Lance
from ..model.produto import Produto
from ..model.vendedor import Vendedor
from ..model.comprador import Comprador


class Controller:
    def __init__(self):
        self.leilao = None
        self.maior_lance = None

    def cria_leilao(self, nome_vendedor: str, nome_produto: str, preco_inicial: float):
        vendedor = Vendedor(nome_vendedor)
        produto = Produto(nome_produto, preco_inicial)
        self.leilao = Leilao(vendedor, produto)

    def encerra_leilao(self):
        item = self.leilao.produto
        lance = self.maior_lance
        self.leilao = None
        self.maior_lance = 0
        return item,lance

    def cria_lance(self, nome_comprador:str, preco: float):
        comprador = Comprador(nome_comprador)
        lance = Lance(comprador, preco)
        if self.maior_lance is None or preco > self.maior_lance.preco:
            self.leilao.criar_lance(lance)
            self.maior_lance = lance
