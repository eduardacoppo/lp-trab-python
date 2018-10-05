class Veiculos(object):

   def __init__(self, sigla, nome, tipo, fator_impacto, issn):
      self.sigla = sigla
      self.nome = nome
      self.tipo = tipo
      self.fator_impacto = fator_impacto
      self.issn = issn
      self.anos = []
      self.qualis = []
      
   def defineQualis(self, ano, qualis):
      self.anos.append(ano)
      self.qualis.append(qualis)

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
      for i in self.anos:
         retorno += str(i);
         retorno += '-'
      retorno += ', '

      for i in self.qualis:
         retorno += i;
         retorno += '-'
      
      return retorno
