from sklearn.cluster import KMeans
import pandas as pd

csv = pd.read_csv('dados.csv', sep=',')
csv = csv.drop(columns=['id', 'tipo', 'data_publicacao', 'num_reacoes'])
dados = csv.values

modelo = KMeans(3)
modelo.fit(dados)

print('Informe os dados da postagem para que seja dito o grupo vinculado')
print('')

numComent = int(input('Número de Comentários: '))
numCompart = int(input('Número de Compartilhamentos: '))
numLikes = int(input('Número de Likes: '))
numLoves = int(input('Número de Loves: '))
numWows = int(input('Número de Wows: '))
numRisos = int(input('Número de Risos: '))
numCarinTris = int(input('Número de Carinha Triste: '))
numRaiva = int(input('Número de Raiva: '))

novosDados = [
    [numComent, numCompart, numLikes, numLoves, numWows, numRisos, numCarinTris, numRaiva]
]

resultado = modelo.predict(novosDados)
print('')
print(f'Grupo: {int(resultado[0])}')
