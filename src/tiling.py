import subprocess

# /home/juju/pythonvenvgridDE/bin/python ./src/tiling.py /usr/bin/python3 /home/juju/workspace/tiled-grid-germany-zensus2011/src/tiling.py


def tiling(code, a, t):
    print(code + " " + str(a * 100) + "m")

    # gridtiler -i ./input/out_ALTER_KURZ.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a = c.grd_id.split('N')[1].split('E'); return { x:100*a[1],y:100*a[0] };" -m "delete c.grd_id" -a 1 -o ./out/ALTER_KURZcsv/100m/ -e csv

    subprocess.run(
        [
            "gridtiler",
            "-i",
            "./input/out_" + code + ".csv",
            "-r",
            "100",
            "-c",
            "3035",
            "-x",
            "3900000",
            "-y",
            "2600000",
            "-p",
            "const a = c.grd_id.split('N')[1].split('E'); return { x:100*a[1],y:100*a[0] };",
            "-m",
            "delete c.grd_id",
            "-a",
            str(a),
            "-o",
            "./out/" + code + "csv/" + str(a * 100) + "m/",
            "-t",
            str(t),
            "-e",
            "csv",
        ]
    )


# increase javascript heap size
# export NODE_OPTIONS="--max-old-space-size=16384"
# subprocess.run(['export NODE_OPTIONS="--max-old-space-size=16384"'])

for code in [
    "INSGESAMT",
    "ALTER_KURZ",
    "FAMSTND_AUSF",
    "GEBURTLAND_GRP",
    "GESCHLECHT",
    "RELIGION_KURZ",
    "STAATSANGE_GRP",
    "GEBTYPBAUWEISE",
    "BAUJAHR_MZ",
    "HEIZTYP",
]:
    for a in [1, 2, 5, 10, 20, 50, 100, 200, 500]:
        t = 256 if code == "INSGESAMT" else 128
        tiling(code, a, t)
