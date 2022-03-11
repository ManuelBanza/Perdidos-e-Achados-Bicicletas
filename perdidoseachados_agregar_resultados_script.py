import time
import pandas as pd
from datetime import datetime
from datetime import date
import glob

# Agregar datasets
path = r'data_sources/data_transformed' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.drop_duplicates(subset='NR_REGISTO', keep="first", inplace=True)

frame.to_csv('data_sources/output/tabela_bicicletas_encontradas.csv', index=False)