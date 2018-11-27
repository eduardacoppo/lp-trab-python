from Publicacoes import Publicacoes

class Periodico(Publicacoes):
#inheritance here
    def __init__(self,volume, ano, veiculo, titulo, autores, numero, pg_inicial, pg_final):
        super(Periodico,self).__init__(ano, veiculo, titulo, autores, numero, pg_inicial, pg_final)
        self.volume = volume
