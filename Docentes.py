class Docentes(object):


    def __init__(self, nome, codigo, data_nascimento, data_ingresso, coordenador):
        self.nome = nome
        self.codigo = codigo
        self.data_nascimento = data_nascimento
        self.data_ingresso = data_ingresso
        self.coordenador = coordenador

    def __str__(self):
        retorno = self.nome
        retorno += ', '
        retorno += str(self.codigo)
        retorno += ', '
        retorno += str(self.data_nascimento)
        retorno += ', '
        retorno += str(self.data_ingresso)
        retorno += ', '
        retorno += str(self.coordenador)

        return retorno