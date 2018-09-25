import csv
from Docentes import Docentes
from datetime import datetime

def main():
    le_arquivo_docentes()

def le_arquivo_docentes():
    path = 'docentes.csv'
    file = open(path, newline='')
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


    print("DOCENTES")
    print(header)
    for i in listaDocentes:
        print(i)
    
    return listaDocentes

main()
