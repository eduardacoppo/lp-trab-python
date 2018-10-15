import csv
from Docentes import Docentes
from Veiculos import Veiculos

from datetime import datetime
from functools import reduce

def main():
    listaDocentes = le_arquivo_docentes()
    listaVeiculos = lerArquivoVeiculos()
    lerArquivoQualis(listaVeiculos)
    print("DOCENTES")

    for i in listaDocentes:
        print(i)
    
    print("VEICULOS")

    for i in listaVeiculos:
        print(i)
        
def le_arquivo_docentes():
    path = 'docentes.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaDocentes = []
    for row in reader:
        codigo = str(row[0])
        nome = str(row[1])
        data_nascimento = datetime.strptime(row[2], '%d/%m/%Y')
        data_ingresso = datetime.strptime(row[3], '%d/%m/%Y')
        coordenador = str(row[4]) == 'X'

        docente = Docentes(nome, codigo, data_nascimento, data_ingresso, coordenador)
        listaDocentes.append(docente)

    return listaDocentes

def lerArquivoVeiculos():
    path = 'veiculos.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaVeiculos = []
    for row in reader:
        sigla = str(row[0])
        nome = str(row[1])
        tipo = str(row[2])
        fator = float(str(row[3]).replace(',','.'))
        issn = str(row[4])

        veiculo = Veiculos(sigla, nome, tipo, fator, issn)
        listaVeiculos.append(veiculo)

    return listaVeiculos

def lerArquivoQualis(listaVeiculos):
    path = 'qualis.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha

    for row in reader:
        ano = int(str(row[0]))
        qualis = str(row[2])
        for i in listaVeiculos:
            if i.sigla == str(row[1]):
                i.anoSet(ano)
                i.qualisSet(qualis)
                print(ano, qualis, i)
        
        
main()


