from dataclasses import dataclass
from .comprador import Comprador


@dataclass
class Lance:
    comprador: Comprador
    preco: float