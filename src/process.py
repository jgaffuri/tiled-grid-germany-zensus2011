#!/home/juju/pythonvenvgridDE/bin python

#/home/juju/pythonvenvgridDE/bin/python ./src/process.py /usr/bin/python3 /home/juju/workspace/tiled-grid-germany-zensus2011/src/process.py

import pandas as pd

# see https://saturncloud.io/blog/how-to-use-pandas-with-jupyter-notebooks/
# https://reproducible-science-curriculum.github.io/sharing-RR-Jupyter/01-sharing-github/
# https://github.com/wahlatlas/grid_data/blob/main/gridviz_tiled_csv.ipynb


print("Hallo Welt !")


griddf = pd.read_csv("input/csv_Demographie_100m_Gitter/Bevoelkerung100M.csv", sep=';', encoding='iso-8859-1')
#charset=iso-8859-1

#griddf.head(3)

