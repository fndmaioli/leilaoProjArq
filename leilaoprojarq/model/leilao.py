from dataclasses import dataclass, field
from typing import Dict, List
from collections import defaultdict

from .lance import Lance
from .produto import Produto
from .vendedor import Vendedor


@dataclass
class Leilao:
    vendedor: Vendedor
    lances: Dict[str, List[Lance]] = field(init=False, default_factory=lambda: defaultdict(list))
    produto: Produto
    
    def criar_lance(self, lance: Lance):
        self.lances[lance.comprador.nome].append(lance)
