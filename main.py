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
    listaDocentes = ler_arquivo_docentes()
    listaVeiculos = ler_arquivo_veiculos()
    listaPubicacoes = ler_arquivo_publicacoes(listaVeiculos,listaDocentes)
    listaQualificacoes = ler_arquivo_qualis(listaVeiculos)
    regras = ler_arquivo_regras()

    
    write_lista_publicacoes(listaPubicacoes)
    write_estatisticas(listaPubicacoes)

def ler_arquivo_docentes():
    path = 'docentes.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaDocentes = []
    listaCodigos =[]

    for row in reader:
        codigo = str(row[0]).strip()
        nome = str(row[1]).strip()
        data_nascimento = datetime.strptime(row[2], '%d/%m/%Y')
        data_ingresso = datetime.strptime(row[3], '%d/%m/%Y')
        coordenador = str(row[4]) == 'X'
        listaCodigos.append(codigo)
        docente = Docentes(nome, codigo, data_nascimento, data_ingresso, coordenador)
        listaDocentes.append(docente)
    
    return listaDocentes

def ler_arquivo_veiculos():
    path = 'veiculos.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaVeiculos = []
    listaSiglas =[]
    for row in reader:
        sigla = str(row[0]).strip()
        nome = str(row[1]).strip()
        tipo = str(row[2]).strip()
        fator = float(str(row[3]).replace(',','.'))
        issn = str(row[4]).strip()
        listaSiglas.append(sigla)
        veiculo = Veiculos(sigla, nome, tipo, fator, issn)
        listaVeiculos.append(veiculo)

    return listaVeiculos

def ler_arquivo_publicacoes(listaVeiculos,listaDocentes):
    path = 'publicacoes.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaPubicacoes =[]
    listaAutores =[]
    for row in reader:
        ano = int(row[0])
        siglaVeiculo = str(row[1]).strip() 
        # apartir da sigla lida encontrar o veiculo
        for v in listaVeiculos:
            if v.sigla == siglaVeiculo:
                veiculo = v
        titulo = str(row[2]).strip()
        autores = row[3].split(',') 
        for docente in listaDocentes:
            for autor in autores:
                if autor.strip() == docente.codigo:
                    listaAutores.append(docente)    
        numero = int(row[4])
        volume = str(row[5]).strip()
        local = str(row[6]).strip()
        pagina_inicial = int(row[7])
        pagina_final = int(row[8])
        if veiculo.tipo == 'C' or veiculo.tipo == 'c':
            conferencia = Conferencia(local,ano,veiculo,titulo,listaAutores, numero, pagina_inicial, pagina_final)
            listaPubicacoes.append(conferencia)
            listaAutores =[] # zerar a lista depois de pasar para a publicacao
           
        elif veiculo.tipo == 'P' or veiculo.tipo == 'p':
            volume = int(volume)
            periodico = Periodico(volume,ano,veiculo,titulo,listaAutores, numero, pagina_inicial, pagina_final)
            listaPubicacoes.append(periodico)
            listaAutores =[] # zerar a lista depois de pasar para a publicacao
    
            
    return listaPubicacoes

def ler_arquivo_qualis(listaVeiculos):
    path = 'qualis.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    
    listaQualificacoes = []
    for row in reader:
        ano = int(row[0])
        sigla = str(row[1]).strip() 
        qualis = str(row[2]).strip()
        veiculo=''
        for v in listaVeiculos:
            if v.sigla == sigla:
                veiculo = v
                veiculo.qualisSet(qualis)
                veiculo.anoSet(ano)
        
        qualificacao = Qualificacao(ano,veiculo,qualis)
        
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

    regras = Regras(multiplicador,data_inicio,data_fim,anos_considerar,minimo_pontos,ponto_regra)
    return regras

def write_lista_publicacoes(listaPubicacoes):

    listaPubicacoes.sort(key=lambda x: x.titulo) # sort by titulo
    listaPubicacoes.sort(key=lambda y: y.veiculo.sigla) # sort by veiculo
    listaPubicacoes.sort(key=lambda z: z.ano, reverse=True) # sort by ano
    listaPubicacoes.sort(key=lambda k: k.veiculo.qualis) #sort by qualis

    with open('2-publicacoes.csv','w', newline='',encoding="utf8") as csv_file:
        fieldnames = ['Ano','Sigla Veículo','Veículo','Qualis','Fator de Impacto','Título','Docentes']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,delimiter = ';')

        writer.writeheader()
        for i in listaPubicacoes:
            writer.writerow({'Ano': i.ano, 'Sigla Veículo': i.veiculo.sigla, 'Veículo': i.veiculo.nome,
            'Qualis': i.veiculo.qualis,'Fator de Impacto': i.veiculo.fator_impacto,
            'Título': i.titulo,'Docentes': [autor.nome for autor in i.autores]})

# retorna uma lista com todas as publicacoes com determinado qualis
def getAllByQualis(qualis,listaPublicacoes):
        listaPub = []

        for pub in listaPublicacoes:
            if pub.veiculo.qualis == qualis:
                listaPub.append(pub)

        return listaPub

#retorna o ratio de publiccacoes com determinado qualis por docente    
def getRatioByQualis(qualis,listaPublicacoes):
    soma =0
    
    for pub in listaPublicacoes:
        if pub.veiculo.qualis == qualis:
            soma += 1.0/len(pub.autores)
            
    return soma             

def write_estatisticas(listaPubicacoes):

    possibleQualis = [ 'A1', 'A2', 'B1', 'B2', 'B3', 'B4', 'B5', 'C']
    pubArray =[]

    with open('3-estatisticas.csv','w', newline='',encoding="utf8") as csv_file:
        fieldnames = ['Qualis','Qtd. Artigos','Média Artigos / Docente']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames,delimiter = ';')

        writer.writeheader()
        for q in possibleQualis:
          pubArray =  getAllByQualis(q,listaPubicacoes)
          ratio =   getRatioByQualis(q,listaPubicacoes)
          writer.writerow({'Qualis': q, 'Qtd. Artigos':len(pubArray),'Média Artigos / Docente': ratio})

main()


