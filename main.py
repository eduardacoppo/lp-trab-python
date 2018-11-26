import csv
from Docentes import Docentes
from Veiculos import Veiculos
from Regras import Regras

from datetime import datetime
from functools import reduce

def main():
    MapDocentes = ler_arquivo_docentes()
    MapVeiculos = ler_arquivo_veiculos()
    listaPubicacoes = ler_arquivo_publicacoes()
    ler_arquivo_qualis(MapVeiculos)
    regras = ler_arquivo_regras()


    write_lista_publicacoes()
    write_estatisticas()

def ler_arquivo_docentes():
    path = 'docentes.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaDocentes = []
    listaCodigos =[]

    for row in reader:
        codigo = str(row[0])
        nome = str(row[1])
        data_nascimento = datetime.strptime(row[2], '%d/%m/%Y')
        data_ingresso = datetime.strptime(row[3], '%d/%m/%Y')
        coordenador = str(row[4]) == 'X'
        listaCodigos.append(codigo)
        docente = Docentes(nome, codigo, data_nascimento, data_ingresso, coordenador)
        listaDocentes.append(docente)
    
    MapDocente = dict(zip(listaCodigos,listaDocentes)) #dicionario cod -> docente
    print(listaCodigos[0],MapDocente.get(listaCodigos[0]).nome) #test
    return MapDocente

def ler_arquivo_veiculos():
    path = 'veiculos.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaVeiculos = []
    listaSiglas =[]
    for row in reader:
        sigla = str(row[0])
        nome = str(row[1])
        tipo = str(row[2])
        fator = float(str(row[3]).replace(',','.'))
        issn = str(row[4])
        listaSiglas.append(sigla)
        veiculo = Veiculos(sigla, nome, tipo, fator, issn)
        listaVeiculos.append(veiculo)
    
    MapVeiculos = dict(zip(listaSiglas,listaVeiculos))
    return MapVeiculos

#not finalized
def ler_arquivo_publicacoes():
    path = 'publicacoes.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaPubicacoes =[]

    for row in reader:
        ano = row[0]
        nomeVeiculo = row[1] #procurar o veiculo pelo nome para associalo com a publicacao
        titulo = row[2]
        autores = row[3] # autores sao da lista de docentes ?
        numero = row[4]
        # verificar se volume e local de conferencia precisa estar em publicacoes (I think so)
        pagina_inicial = row[6]
        pagina_final = row[7]

        pass
    return listaPubicacoes

#not finalized
def ler_arquivo_qualis(MapVeiculos):
    path = 'qualis.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha

    for row in reader:
        ano = int(str(row[0]))
        sigla = row[1] #find the veiculo associate with it through an object qualis ?
        qualis = str(row[2])
        #criar um objeto qualis
        
        
def ler_arquivo_regras(): 
    path ='regras.csv'   
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    for row in reader:
        data_inicio = datetime.strptime(row[0], '%d/%m/%Y')
        data_fim = datetime.strptime(row[1], '%d/%m/%Y')
        qualis = row[2].split(',')
        score = row[3].split(',')
        ponto_regra  = dict(zip(qualis,score))
        #print(ponto_regra)
        multiplicador = row[4]
        anos_considerar = row[5]
        minimo_pontos = row[6]

        #print( multiplicador,anos_considerar,minimo_pontos)
    regras = Regras(multiplicador,data_inicio,data_fim,anos_considerar,minimo_pontos,ponto_regra)
    return regras

def write_lista_publicacoes():
    print('this is from the lista de publicacoes function !!!')

def write_estatisticas():
    pass

main()


