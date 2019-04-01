def vendedor_fluxo():
    v = -1
    while v != 0:
        v = int(input("0-Sair\n1-Criar Leilao\n2-Encerrar Leilao\n"))
        if v == 1:
            # controller cria leilao
        elif v == 2:
            # controller encerra leilao
            
def comprador_fluxo():
    v = -1
    while v != 0:
        v = int(input("0-Sair\n1-Dar lance\n"))
        if v == 1:
            #controller dar lance

def main():
    v = -1
    while v != 0:
        v = int(input("0-Sair\n1-Vendedor\n2-Comprador\n"))
        if v == 1:
            vendedor_fluxo()
        elif v == 2:
            comprador_fluxo()

if __name__ == '__main__':
    main()