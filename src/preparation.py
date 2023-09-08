#!/home/juju/pythonvenvgridDE/bin python

# /home/juju/pythonvenvgridDE/bin/python ./src/preparation.py /usr/bin/python3 /home/juju/workspace/tiled-grid-germany-zensus2011/src/preparation.py

import pandas as pd
import numpy as np


def prepare(csvfile, sep, code, printfinal):
    print(code)

    print("Load data")
    df = pd.read_csv(csvfile, sep=sep, encoding="iso-8859-1") #, nrows=10000)

    print("drop unecessary rows")
    df = df[df.Merkmal == code]

    print("drop unecessary columns")
    df = df.drop(["Gitter_ID_100m_neu", "Auspraegung_Text", "Anzahl_q", "Merkmal"], axis=1)

    print("Make new grd_id column")
    df["grd_id"] = df.apply(
        lambda row: row["Gitter_ID_100m"].replace("100m", ""), axis=1
    )

    print("Drop unecessary column Gitter_ID_100m")
    df = df.drop(["Gitter_ID_100m"], axis=1)

    print("Rename Anzahl column")
    df = df.rename(columns={"Anzahl": "value"})

    print("Pivot")
    df = pd.pivot_table(
        df,
        columns=["Auspraegung_Code"],
        values="value",
        index=["grd_id"],
        aggfunc=np.sum,
        fill_value=0,
    )

    if printfinal:
        print(df)

    print("Save")
    df.to_csv("input/out_" + code + ".csv")

    print("Done " + code)


printfinal = False
csvfileDemo = "input/csv_Demographie_100m_Gitter/Bevoelkerung100M.csv"
prepare(csvfileDemo, ";", " INSGESAMT", printfinal)
prepare(csvfileDemo, ";", "ALTER_KURZ", printfinal)
prepare(csvfileDemo, ";", "FAMSTND_AUSF", printfinal)
prepare(csvfileDemo, ";", "GEBURTLAND_GRP", printfinal)
prepare(csvfileDemo, ";", "GESCHLECHT", printfinal)
prepare(csvfileDemo, ";", "RELIGION_KURZ", printfinal)
prepare(csvfileDemo, ";", "STAATSANGE_GRP", printfinal)
#TODO rename "out_ INSGESAMT.csv" into "out_INSGESAMT.csv"

csvfileHab = "input/csv_Wohnungen_100m_Gitter/Wohnungen100m.csv"
prepare(csvfileHab, ",", "GEBTYPBAUWEISE", printfinal)
prepare(csvfileHab, ",", "BAUJAHR_MZ", printfinal)
prepare(csvfileHab, ",", "HEIZTYP", printfinal)
