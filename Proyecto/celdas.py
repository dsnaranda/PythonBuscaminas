class Celda:
    def __init__(self):
        self.es_mina = False
        self.revelada = False
        self.marcada = False
        self.minas_alrededor = 0

    def __str__(self):
        if self.marcada:
            return "M"
        if not self.revelada:
            return "-"
        if self.es_mina:
            return "*"
        return str(self.minas_alrededor)