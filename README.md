# Tiled grid for Germany zensus 2011

Download input data from: https://www.zensus2011.de/DE/Home/Aktuelles/DemografischeGrunddaten.html?nn=559100#Gitter
Store it in a *input* folder at the root of the project.

The downloaded data can be proccessed with the python scripts:
  1. `preparation.py` to extract and format the data into CSV files created at the root of the `input/` folder.
  2. `tiling.py` to extract and format these files. [gridtiler](https://github.com/eurostat/gridtiler) need to be installed. The output is stored in the `out/` folder.

## Copyright

Data is ©Statistisches Bundesamt, Wiesbaden 2018. Reproduction and distribution, also of parts, are permitted provided that the source is mentioned.
