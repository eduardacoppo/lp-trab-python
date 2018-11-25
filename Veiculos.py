class Veiculos(object):

   
   def __init__(self, sigla, nome, tipo, fator_impacto, issn):
      self.sigla = sigla
      self.nome = nome
      self.tipo = tipo
      self.fator_impacto = fator_impacto
      self.issn = issn
      self.ano = 0
      self.qualis = ''
      
   def anoSet(self, ano):
      self.ano = ano

   def qualisSet(self, qualis):
      self.qualis = qualis

   def __str__(self):
      retorno = self.sigla
      retorno += ', '
      retorno += self.nome
      retorno += ', '
      retorno += self.tipo
      retorno += ', '
      retorno += str(self.fator_impacto)
      retorno += ', '
      retorno += self.issn
      retorno += ', '
      retorno += str(self.ano)
      retorno += ', '
      retorno += self.qualis
      
      return retorno
