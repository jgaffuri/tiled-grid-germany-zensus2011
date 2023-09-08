import subprocess


def tiling(code):
    print(code)

    # -i ./input/csv_Demographie_100m_Gitter/out_demo.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a=c.grd_id.split('N')[1].split('E');return {x:100*a[1],y:100*a[0]};" -m "delete c.grd_id" -a 1 -o ./out/demo/100m/ -e parquet

    subprocess.run(["gridtiler", "-i", "./dddd/"])

