import pandas as pd

lista_nomes = 'Joao Maria Jose Jean'.split()
lista_idades = '25, 26, 27, 28'.split()
lista_salarios = '1000, 2000, 3000, 4000'.split()

nomes = pd.DataFrame(lista_nomes, columns=['NOME'])

print(nomes)

dados = list(zip(lista_nomes, lista_idades, lista_salarios))

tuplas = pd.DataFrame(dados, columns=['nome', 'idade', 'salarios',])

print()
print(tuplas)