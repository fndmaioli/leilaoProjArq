from dataclasses import dataclass

@dataclass
class Leilao:
    vendedor
    lances
    produto

    def encerrar_leilao(self):
        pass
    
    def criar_lance(self, lance):
        lances.append(lance)
        pass
    
