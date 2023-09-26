class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, 'Bateu a meta.')
        else:
            print(self.nome, 'Não bateu a meta.')

vendedor1 = Vendedor('Matheus')
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)

vendedor2 = Vendedor('João')
vendedor1.vendeu(300)
vendedor1.bateu_meta(600)