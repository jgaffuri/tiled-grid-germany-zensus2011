# Tiled grid for Germany zensus 2011




Download input data from: https://www.zensus2011.de/DE/Home/Aktuelles/DemografischeGrunddaten.html?nn=559100#Gitter
Store it in a *input* folder at the root of the project.

The downloaded data is handled in the `process_*.py` python script. This process extracts and formats the necessary data into a CSV file. This CSV file is then tiled based on [gridtiler](https://github.com/eurostat/gridtiler) - see the corresponding `tiling_*.sh` script. The output is stored in the `out/` folder.

## Copyright

Data is ©Statistisches Bundesamt, Wiesbaden 2018. Reproduction and distribution, also of parts, are permitted provided that the source is mentioned.
