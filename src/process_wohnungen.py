#!/home/juju/pythonvenvgridDE/bin python

#/home/juju/pythonvenvgridDE/bin/python ./src/process_wohnungen.py /usr/bin/python3 /home/juju/workspace/tiled-grid-germany-zensus2011/src/process_wohnungen.py

import pandas as pd
import numpy as np

# see https://saturncloud.io/blog/how-to-use-pandas-with-jupyter-notebooks/
# https://reproducible-science-curriculum.github.io/sharing-RR-Jupyter/01-sharing-github/
# https://github.com/wahlatlas/grid_data/blob/main/gridviz_tiled_csv.ipynb


csvfile = "input/csv_Wohnungen_100m_Gitter/Wohnungen100m.csv"
csvfileout = "input/csv_Wohnungen_100m_Gitter/out.csv"

print("Load data")
df = pd.read_csv(csvfile, sep=',', encoding='iso-8859-1', nrows=10000)

print("drop unecessary columns")
df = df.drop(['Gitter_ID_100m_neu', 'Auspraegung_Text', 'Anzahl_q'], axis=1)

print("modify Merkmal column")
df['Merkmal'] = df.apply(lambda row: row["Merkmal"].replace(' INSGESAMT', 'INSGESAMT'), axis=1)

print("Make new variable column")
df['variable'] = df.apply(lambda row: row["Merkmal"] + "_" + str(row["Auspraegung_Code"]), axis=1)

print("Drop unecessary columns")
df = df.drop(['Merkmal', 'Auspraegung_Code'], axis=1)

print("Make new grd_id column")
df['grd_id'] = df.apply(lambda row: row["Gitter_ID_100m"].replace('100m', ''), axis=1)

print("Drop unecessary column")
df = df.drop(['Gitter_ID_100m'], axis=1)

print("Rename Anzahl column")
df = df.rename(columns={"Anzahl": "value"})

print("Pivot")
#.groupby("grd_id").pivot("variable", ["value"])
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html
df = pd.pivot_table(df, columns=['variable'], values='value', index=['grd_id'], aggfunc=np.sum, fill_value=0)

#print("Round")
#df = df.round()

#print(df)

print("Save")
df.to_csv(csvfileout)  

print("Done")
