class Plataforma:
    def __init__(self, nome, id = None, imagem = None):
        self.nome = nome
        self.id_plataforma = id
        self.imagem = imagem

    def __str__(self):
        return f'Plataforma: {self.nome}'

class Jogo:
    def __init__(self, nome, plataforma, id = None, completo = 0.0, capa = None):
        self.id_jogo = id
        self.nome = nome
        self.completo = completo
        self.capa = capa
        self.plataforma = plataforma

    def __str__(self):
        return f'Nome do jogo: {self.nome}, da plataforma: {self.plataforma}'