# EXECUTE ESSE ARQUIVO PARA QUE POSSA SER GERADO UM DATAFRAME QUE CONTENHA OS DADOS DAS IMAGENS
# COMO O ID DA BEXIGA, PESO, CAMINHO PARA ACESSAR A IMAGEM

import pandas as pd
import os

# Cria um a lista com todas as pastas que contém imagens
lista_pastas = [pasta for pasta in os.listdir() if os.path.isdir(pasta) and pasta != '.git']

# Cria uma lista com o caminho de cada imagem
lista_caminho_imagens = []
for pasta in lista_pastas: lista_caminho_imagens.extend(list(map(lambda x: os.path.join(pasta, x), os.listdir(pasta))))

# Remove o caminho das imagens que contém o nome 'balança'
lista_caminho_imagens = list(filter(lambda x: x if 'balança' not in x else None, lista_caminho_imagens))

# Ordena a lista de acordo com o ID da bexiga
lista_caminho_imagens = sorted(lista_caminho_imagens, key = lambda x: int(x.split('_')[0]))

# Cria uma lista com o ID da beixga de cada imagem
lista_id = [int(idbexiga.split('_')[0]) for idbexiga in lista_caminho_imagens]

# Cria uma lista com o peso da bexiga de cada imagem
lista_peso = [int(peso.split('_')[1].split('/')[0]) for peso in lista_caminho_imagens]

# Cria uma lista com o nome de cada imagem
lista_imagem = [os.path.basename(imagem) for imagem in lista_caminho_imagens]

# Cria uma lista com o caminho absoluto de cada imagem
lista_caminho_imagens = [os.path.abspath(imagem) for imagem in lista_caminho_imagens]

# Cria um dicionário com os dados das imagens
dados = {"caminho_imagem": lista_caminho_imagens,
         "imagem": lista_imagem,
         "id_bexiga": lista_id,
         "peso_bexiga": lista_peso}

# Cria o dataframe com os dados das imagens
df_imagem = pd.DataFrame(dados)

# Salva o dataframe no formato .parquet
df_imagem.to_parquet(path = "df_imagem.parquet")