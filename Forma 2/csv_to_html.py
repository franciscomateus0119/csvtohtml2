#Author: Francisco Mateus Rocha Filho
#Date: 03/02/2020 (3 de fevereiro de 2020)

import pandas as pd
import os
import glob

pasta = input("Diretório dos arquivos .csv: ")
pasta_destino = input("Diretório onde serão salvos os arquivos .html: ")
tipo = 'csv'
tipo_destino = 'html'

for f in glob.glob(pasta + "/*."+tipo):
    df = pd.read_csv(f)
    df['data'] = pd.to_datetime(df['data'], yearfirst=True, format='%Y/%m').apply(lambda x: x.strftime('%Y-%m'))
    df = df.sort_values(by=['data','valor'], axis=0, ascending=[True,False], inplace=False, kind='quicksort', na_position='last')
    df = df.loc[df.groupby("data")["valor"].idxmax()]
    df.to_html(pasta_destino + "/" + os.path.splitext(os.path.basename(f))[0] + "." + tipo_destino, index=False)