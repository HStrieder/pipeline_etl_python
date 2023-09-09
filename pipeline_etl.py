import pandas as pd
import sqlite3

#Criação de um arquivo CSV de dados brutos de exemplo, pode ser substituido por outro arquivo CSV.
dados_brutos = pd.DataFrame({
    'Data': ['2023-09-05', '2023-09-06', '2023-09-07'],
    'SensorID': [1,2,3],
    'Leitura':[55,45,60],
    'Localizacao':['Local A', 'Local B', 'Local C']
})

dados_brutos.to_csv('dados_brutos.csv', index=False)

#EXTRAÇÃO

dados_brutos = pd.read_csv('dados_brutos.csv')

#TRANSFORMAÇÃO

dados_transformados = dados_brutos[dados_brutos['Leitura'] > 50]

#CARREGAMENTO ~ LOADING

conexao = sqlite3.connect('monitoramento_qualidade_ar.db')
dados_transformados.to_sql('leituras_sensores', conexao, if_exists='replace', index=False)

#fechando a conexao com o banco de dados
conexao.close()

#consulta dos dados carregados no banco de dados SQLite
conexao = sqlite3.connect('monitoramento_qualidade_ar.db')
consulta = pd.read_sql_query('SELECT * FROM leituras_sensores',conexao)
conexao.close()

print('\nDados carregados no banco de dados:')
print(consulta)


