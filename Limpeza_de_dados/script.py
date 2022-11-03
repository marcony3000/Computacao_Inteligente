import pandas as pd #para ler, visualizar e printar infos do df
import matplotlib.pyplot as plt #para construir e customizar gráficos
import seaborn as sns #para visualizar uns gráficos
import numpy as np #numpy porque é sempre bom importar numpy né 


df = pd.read_csv('spotify.csv', index_col=0) #Aqui estamos definindo que o arquivo ficará guardado no nome "df"
df.sort_values('song_popularity', ascending=False, inplace=True) #Deixa as músicas em ordem de popularidade
df.head(15) #aqui definimos que as primeiras 15 linhas aparecerão
print(df) 

print('Vizualizar DF')
df.head() #para visualizar o começo do seu dataframe
print(df)

print('Vizualizar Informações')
df.info() #para obter informações do seu dataframe
print(df)

print('Vizualizar Descrição detalhada do DF')
df.describe() #para ver um descrição mais detalhada
print(df)

print('Verificar os duplicados')
duplicados = df[df.duplicated(keep='first')]
print(duplicados)

print ('Excluindo os dados duplicados')
df.drop_duplicates(keep='first', inplace=True) 


print('Removendo unidades de medidas')
def remove_units (DataFrame, columns, what):
    for col in columns:
        DataFrame[col] = DataFrame[col].str.strip(what)
 
remove_units(df, ['acousticness', 'danceability'], 'mol/L')
remove_units(df, ['song_duration_ms', 'acousticness'], 'kg')
print(df)

print('Decodificar os valores')
type(np.nan)

print('Trocando dados faltantes')

df = df.replace(['nao_sei'], np.nan)
df['key'] = df['key'].replace([0.177], np.nan)
df['audio_mode'] = df['audio_mode'].replace(['0.105'], np.nan)
df['speechiness'] = df['speechiness'].replace(['0.nao_sei'], np.nan)
df['time_signature'] = df['time_signature'].replace(['0.7', '2800000000'], np.nan)

print('Datatypes')
print('Ajustar tipos de variáveis')

numerical_cols = ['song_duration_ms', 'acousticness', 'danceability',
                  'energy', 'instrumentalness', 'liveness', 'loudness',
                  'speechiness', 'tempo', 'audio_valence']
 
categorical_cols = ['song_popularity', 'key', 'audio_mode', 'time_signature']
 
def to_type(DataFrame, columns, type):
    for col in columns:
        DataFrame[col] = DataFrame[col].astype(type)
 
to_type(df, numerical_cols, 'float')
to_type(df, categorical_cols, 'category')

print(df)


print('Excluindo Outliers')
def exclui_outliers(DataFrame, col_name):
  intervalo = 2.7*DataFrame[col_name].std()
  media = DataFrame[col_name].mean()
  DataFrame.loc[df[col_name] < (media - intervalo), col_name] = np.nan
  DataFrame.loc[df[col_name] > (media + intervalo), col_name] = np.nan

  print(df)


print('Separar colunas numéricas e removendo os outliers')

numerical_cols = ['song_duration_ms', 'acousticness', 'danceability',
                  'energy', 'instrumentalness', 'liveness', 
                  'loudness', 'speechiness', 'tempo','audio_valence']
for col in numerical_cols:
  exclui_outliers(df, col)

print('Passa por algumas colunas e substitui os valores faltantes')

for column in ['acousticness', 'liveness', 'speechiness']:
    df[column].fillna(df[column].mode()[0], inplace=True)
print(df)

print('vamos substituir os valores nas outras coluna pela mediana')

for column in ['song_duration_ms',  'danceability', 'energy', 
                'loudness', 'audio_valence']:
    df[column].fillna(df[column].mean(), inplace=True)

print(df)


print('Excluir as linhas com dados faltantes')
df.dropna(inplace=True)
print(df)