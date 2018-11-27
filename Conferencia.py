from Publicacoes import Publicacoes

class Conferencia(Publicacoes):
#inheritance here
    def __init__(self,local,ano, veiculo, titulo, autores, numero, pg_inicial, pg_final):
        super(Conferencia,self).__init__(ano, veiculo, titulo, autores, numero, pg_inicial, pg_final)
        self.local = local
        
