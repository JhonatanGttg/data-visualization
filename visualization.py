import cufflinks as cf
from plotly.offline import plot, iplot
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio 
import cufflinks as cf
import chart_studio
cf.go_offline()
import plotly
import plotly.graph_objs as go
import plotly.offline as py
import chart_studio.plotly as pyo


df = pd.DataFrame(np.random.randn(100,4), columns=['A', 'B', 'C', 'D'])

#Mostra os 5 primeiros dados
df.head()

pio.renderers.default = 'colab'

#Mostrar os graficos do Iplot
df.iplot()

#Abaixo será mostrado os tipos de graficos que pode ser usados // Use a função print para executar
df.iplot(kind='scatter', x='A', y='B', mode='markers')

df.sum().iplot(kind='bar')

df['A'].iplot(kind='hist')

df.iplot(kind='box')

df.iplot(kind='spread')

df.iplot(kind='bubble', x='A', y='B', size='C')

df.scatter_matrix()

#Abaixo será usado o mesmo arquivo do data manipulation
arquivo = '/acidentes2021.csv'
dataset = pd.read_csv(arquivo, sep=';', header=0)
print('Base carregada com sucesso')

#Verificando se a base foi carregada 
dataset.head()

#Começando o usar o iplot nos graficos 
dataset.iplot()

''' Para começar a parti dessa etapa você irá 
precisar do arquivo data manipulation que se encontra em 
https://github.com/JhonatanGttg/data-manipulation '''

#Mostrando os dados do dataset novo
dataset_novo.situacao.value_counts().iplot(kind='bar')

dataset_novo.tipo.value_counts().iplot(kind='bar')

#Mostrando só os meses
dataset_novo['data_mes'] = dataset_novo.data.dt.to_period('M').astype(str)

dataset_novo.data_mes.head()

#Numerando cada tipo igual realizamos no data manipulation so que aqui em grande escala
dataset_novo.loc[dataset_novo['tipo'] == 'COLISÃO FRONTAL', 'tipo'] = 0
dataset_novo.loc[dataset_novo['tipo'] == 'COLISÃO TRASEIRA', 'tipo'] = 1
dataset_novo.loc[dataset_novo['tipo'] == 'COLISÃO COM CICLISTA', 'tipo'] = 2
dataset_novo.loc[dataset_novo['tipo'] == 'COLISÃO LATERAL', 'tipo'] = 3
dataset_novo.loc[dataset_novo['tipo'] == 'CHOQUE', 'tipo'] = 4
dataset_novo.loc[dataset_novo['tipo'] == 'COLISÃO TRANSVERSAL', 'tipo'] = 5
dataset_novo.loc[dataset_novo['tipo'] == 'TOMBAMENTO', 'tipo'] = 6
dataset_novo.loc[dataset_novo['tipo'] == 'ATROPELAMENTO', 'tipo'] = 7
dataset_novo.loc[dataset_novo['tipo'] == 'COLISÃO', 'tipo'] = 8
dataset_novo.loc[dataset_novo['tipo'] == 'CAPOTAMENTO', 'tipo'] = 9
dataset_novo.loc[dataset_novo['tipo'] == 'ENGAVETAMENTO', 'tipo'] = 10
dataset_novo.loc[dataset_novo['tipo'] == 'ATROPELAMENTO DE PESSOA', 'tipo'] = 11
dataset_novo.loc[dataset_novo['tipo'] == 'QUEDA', 'tipo'] = 12
dataset_novo.loc[dataset_novo['tipo'] == 'MONITORAMENTO', 'tipo'] = 13
dataset_novo.loc[dataset_novo['tipo'] == 'nan', 'tipo'] = 14
dataset_novo.loc[dataset_novo['tipo'] == 'SEMÁFORO', 'tipo'] = 15
dataset_novo.loc[dataset_novo['tipo'] == 'ATROPELAMENTO DE ANIMAL', 'tipo'] = 16
dataset_novo.loc[dataset_novo['tipo'] == 'ALAGAMENTO', 'tipo'] = 17
dataset_novo.loc[dataset_novo['tipo'] == 'OUTROS APOIOS', 'tipo'] = 18
dataset_novo.loc[dataset_novo['tipo'] == 'APOIO COMPESA', 'tipo'] = 19
dataset_novo.loc[dataset_novo['tipo'] == 'OUTROS', 'tipo'] = 20
dataset_novo['tipo'].unique()

#Convetendo os dados em números
pd.to_numeric(dataset_novo['tipo'])

dataset_novo['tipo'] = dataset_novo['tipo'].astype(float)

acidentes_mes = dataset_novo.groupby(by='data_mes').tipo.sum()

type(acidentes_mes)

acidentes_mes.head()

acidentes_mes.index.item

acidentes_mes.values

data = [go.Scatter(x=acidentes_mes.index,
                   y=acidentes_mes.values)]

#Mostrando os graficos com dados reais de acidentes 

pyo.plot(data)

###################

data = [go.Bar(x=acidentes_mes.index,
               y=acidentes_mes.values,
               marker= {'color': 'lightblue'})]

#criando layout
configuracoes_layout = go.Layout(title='Acidentes por mês',
                                 yaxis={'title': 'Quantidade'},
                                 xaxis={'title': 'Meses'})

#objeto figura

fig = go.Figure(data=data, layout=configuracoes_layout)

#plotando o grafico

py.plot(fig)

##########################

data = [go.Bar(x=acidentes_mes.index,
               y=acidentes_mes.values,
               marker= {'color': 'lightblue',
                        'line': {'color': '#333',
                                 'width': 2}
                        },
               opacity=0.7
               )
        ]

#criando layout
configuracoes_layout = go.Layout(title='Acidentes por mês',
                                 yaxis={'title': 'Quantidade'},
                                 xaxis={'title': 'Meses'})

#objeto figura

fig = go.Figure(data=data, layout=configuracoes_layout)

#plotando o grafico

py.plot(fig)

#Mostrando os resultados

acidentes_mes.index

acidentes_mes

#Apresentando a media 
media = acidentes_mes.values.mean()
print(media)

#Criando os acidentes por mês com cores

for x in acidentes_mes.values :
  if x < media:
    cores.append('lightblue')
  else:
    cores.append('red')

cores

data = [go.Bar(x=acidentes_mes.index,
               y=acidentes_mes.values,
               marker= {'color': cores,
                        'line': {'color': '#333',
                                 'width': 2}
                        },
               opacity=0.7
               )
        ]

#criando layout
configuracoes_layout = go.Layout(title='Acidentes por mês',
                                 yaxis={'title': 'Quantidade'},
                                 xaxis={'title': 'Meses'})

#objeto figura

fig = go.Figure(data=data, layout=configuracoes_layout)

#plotando o grafico
py.iplot(fig)

##########

acidentes_ano_anterior = acidentes_mes - 300.0

data = [go.Bar(x=acidentes_ano_anterior.index,
               y=acidentes_ano_anterior.values,
               name = '2020',
               marker= {'color': 'lightgreen',
                        'line': {'color': '#333',
                                 'width': 2}
                        },
               opacity=0.7
                ),
        
        go.Bar(x=acidentes_mes.index,
               y=acidentes_mes.values,
               marker= {'color': cores,
                        'line': {'color': '#333',
                                 'width': 2}
                        },
               opacity=0.7,
               name = '2021'
                     
                       
               )
        ]

#criando layout
configuracoes_layout = go.Layout(title='Acidentes por mês',
                                 yaxis={'title': 'Quantidades'},
                                 xaxis={'title': 'Meses'},
                                 #texto na barra de destaque
                                 annotations = [{'text': 'Mês destaque de acidentes',
                                                 'x': maximo_de_acidentes,
                                                 'y': maximo_de_acidentes}])
                                 

#objeto figura

fig = go.Figure(data=data, layout=configuracoes_layout)

#plotando o grafico
py.iplot(fig)

##########

#Como o dataset não tem o ID, estamos transformando o index criado pelo pandas em coluna
dataset_novo = dataset_novo.reset_index()

#Agrupando a quantidade de acidentes por Bairro e Tipo
dataset_agrupado = dataset_novo.groupby(by=['bairro', 'tipo']).index.sum()

#Tranformando os dados agrupados em um novo dataset
dataset_agrupado = pd.DataFrame(dataset_agrupado)
dataset_agrupado = dataset_agrupado.reset_index()
#print do novo dataset
dataset_agrupado

fig = go.Figure(data=[go.Scatter(
    x=dataset_agrupado['bairro'], y=dataset_agrupado['tipo'],
    mode='markers',
    marker_size=dataset_agrupado['index']*0.001)
])

#fig.show()
py.iplot(fig)












