class Publicacoes(object):

    def __init__(self, ano, veiculo, titulo, autores, numero,volume, local, pg_inicial, pg_final):
        self.ano = ano
        self.veiculo = veiculo
        self.titulo = titulo
        self.autores = autores
        self.numero = numero
        self.pg_inicial = pg_inicial
        self.pg_final = pg_final
        self.volume = volume
        self.local = local

    def __str__(self):
        retorno = str(self.ano)
        retorno += ', '
        retorno += self.veiculo.nome
        retorno += ', '
        retorno += self.titulo
        retorno += ', '
        for i in self.autores:
            retorno += i.codigo
            retorno += ', '
        retorno += str(self.numero)
        retorno += ', '
        retorno += self.volume
        retorno += ', '
        retorno += str(self.local)
        retorno += ', '
        retorno += str(self.pg_inicial)
        retorno += ', '
        retorno += str(self.pg_final)

        return retorno
