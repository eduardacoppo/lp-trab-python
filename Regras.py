class Publicacoes(object):

    def __init__(self,fator_mult, data_incio, data_fim, qtd_anos, potuacao_minima):
        self.fator_mult = fator_mult
        self.data_incio = data_incio
        self.data_fim = data_fim
        self.qtd_anos = qtd_anos
        self.potuacao_minima = potuacao_minima
        #falta um atributo
        #algo para mapear qualis e pontuacoes das regras
