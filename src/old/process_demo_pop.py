#!/home/juju/pythonvenvgridDE/bin python

#/home/juju/pythonvenvgridDE/bin/python ./src/process_demo_pop.py /usr/bin/python3 /home/juju/workspace/tiled-grid-germany-zensus2011/src/process_demo_pop.py

import pandas as pd
import numpy as np

# see https://saturncloud.io/blog/how-to-use-pandas-with-jupyter-notebooks/
# https://reproducible-science-curriculum.github.io/sharing-RR-Jupyter/01-sharing-github/
# https://github.com/wahlatlas/grid_data/blob/main/gridviz_tiled_csv.ipynb


csvfile = "input/csv_Demographie_100m_Gitter/Bevoelkerung100M.csv"
csvfileout = "input/csv_Demographie_100m_Gitter/out_demo_pop.csv"

print("Load data")
df = pd.read_csv(csvfile, sep=';', encoding='iso-8859-1') #, nrows=10000)

print("drop unecessary columns")
df = df.drop(['Gitter_ID_100m_neu', 'Auspraegung_Text', 'Auspraegung_Code', 'Anzahl_q'], axis=1)

print("filter total population")
df = df.loc[df.Merkmal == " INSGESAMT"]

print("Drop unecessary columns")
df = df.drop(['Merkmal'], axis=1)

print("Make new grd_id column")
df['grd_id'] = df.apply(lambda row: row["Gitter_ID_100m"].replace('100m', ''), axis=1)

print("Drop unecessary column")
df = df.drop(['Gitter_ID_100m'], axis=1)

print("Rename Anzahl column")
df = df.rename(columns={"Anzahl": "pop"})

print("filter population > 0")
df = df[(df['pop'] > 0)]

#print(df)

print("Save")
df.to_csv(csvfileout, index=False)

print("Done")
