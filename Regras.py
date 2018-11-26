class Regras(object):

    def __init__(self,fator_mult, data_incio, data_fim, qtd_anos, potuacao_minima,ponto_regras):
        self.fator_mult = fator_mult
        self.data_incio = data_incio
        self.data_fim = data_fim
        self.qtd_anos = qtd_anos
        self.potuacao_minima = potuacao_minima
        self.ponto_regras = ponto_regras
    
    def __str__(self):
        retorno = self.fator_mult
        retorno += ', '
        retorno += str(self.data_incio)
        retorno += ', '
        retorno += str(self.data_fim)
        retorno += ', '
        retorno += str(self.qtd_anos)
        retorno += ', '
        retorno += str(self.potuacao_minima)
        retorno += ', '
        retorno += str(self.ponto_regras)

        return retorno