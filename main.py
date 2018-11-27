import csv
from Docentes import Docentes
from Veiculos import Veiculos
from Regras import Regras
from Publicacoes import Publicacoes
from Conferencia import Conferencia
from Periodico import Periodico
from Qualificacao import Qualificacao

from datetime import datetime
from functools import reduce

def main():
    mapDocentes = ler_arquivo_docentes()
    mapVeiculos = ler_arquivo_veiculos()
    listaPubicacoes = ler_arquivo_publicacoes(mapVeiculos,mapDocentes)
    listaQualificacoes = ler_arquivo_qualis(mapVeiculos)
    regras = ler_arquivo_regras()

    #print(listaPubicacoes[0].titulo)
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
    #print(listaCodigos[0],MapDocente.get(listaCodigos[0]).nome) #test
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
    
    MapVeiculos= dict(zip(listaSiglas,listaVeiculos))
    #print(listaSiglas[0],MapVeiculos[listaSiglas[0]].nome)
    return MapVeiculos

def ler_arquivo_publicacoes(mapVeiculos,mapDocentes):
    path = 'publicacoes.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaPubicacoes =[]
    listaAutores =[]
    for row in reader:
        ano = int(row[0])
        siglaVeiculo = str(row[1]) #procurar o veiculo pelo nome para associalo com a publicacao
        veiculo = mapVeiculos.get(siglaVeiculo)
        titulo = str(row[2])
        autores = row[3].split(',') # autores sao da lista de docentes ?
        for autor in autores:
            listaAutores.append(mapDocentes.get(autor))    
        numero = int(row[4])
        volume = str(row[5])
        local = str(row[6])
        pagina_inicial = int(row[7])
        pagina_final = int(row[8])
        if veiculo.tipo == 'C' or veiculo.tipo == 'c':
            conferencia = Conferencia(local,ano,veiculo,titulo,listaAutores, numero, pagina_inicial, pagina_final)
            listaPubicacoes.append(conferencia)
            #print(conferencia.titulo) 
        else:
            volume = int(volume)
            periodico = Periodico(volume,ano,veiculo,titulo,listaAutores, numero, pagina_inicial, pagina_final)
            listaPubicacoes.append(periodico)
            #print(periodico.titulo)
            
    return listaPubicacoes

def ler_arquivo_qualis(mapVeiculos):
    path = 'qualis.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    
    listaQualificacoes = []
    for row in reader:
        ano = int(row[0])
        sigla = str(row[1]) 
        veiculo = mapVeiculos.get(sigla)
        qualis = str(row[2])
        qualificacao = Qualificacao(ano,veiculo,qualis)
        #print(qualificacao.ano)
        listaQualificacoes.append(qualificacao)

    return listaQualificacoes
      
def ler_arquivo_regras(): 
    path ='regras.csv'   
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    for row in reader:
        data_inicio = datetime.strptime(row[0], '%d/%m/%Y')
        data_fim = datetime.strptime(row[1], '%d/%m/%Y')
        qualis = str(row[2].split(','))
        score = row[3].split(',')
        score = list(map(int,score)) #converter lista de string to list de inteiros
        ponto_regra  = dict(zip(qualis,score))
        multiplicador = float(row[4].replace(',','.'))
        anos_considerar = int(row[5])
        minimo_pontos = int(row[6])

        #print( multiplicador,anos_considerar,minimo_pontos)
    regras = Regras(multiplicador,data_inicio,data_fim,anos_considerar,minimo_pontos,ponto_regra)
    return regras

def write_lista_publicacoes():
    print('this is from the lista de publicacoes function !!!')

def write_estatisticas():
    pass

main()


