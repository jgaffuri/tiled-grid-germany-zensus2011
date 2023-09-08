#!/bin/bash

#export NODE_OPTIONS="--max-old-space-size=8192"
export NODE_OPTIONS="--max-old-space-size=16384"

#gridtiler -i ./input/csv_Demographie_100m_Gitter/out_demo_pop.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a=c.grd_id.split('N')[1].split('E');return {x:100*a[1],y:100*a[0]};" -m "delete c.grd_id" -a 1 -o ./out/demo_pop/100m/ -e parquet -t 256
#gridtiler -i ./input/csv_Demographie_100m_Gitter/out_demo_pop.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a=c.grd_id.split('N')[1].split('E');return {x:100*a[1],y:100*a[0]};" -m "delete c.grd_id" -a 2 -o ./out/demo_pop/200m/ -e parquet -t 256
#gridtiler -i ./input/csv_Demographie_100m_Gitter/out_demo_pop.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a=c.grd_id.split('N')[1].split('E');return {x:100*a[1],y:100*a[0]};" -m "delete c.grd_id" -a 5 -o ./out/demo_pop/500m/ -e parquet -t 256
#gridtiler -i ./input/csv_Demographie_100m_Gitter/out_demo_pop.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a=c.grd_id.split('N')[1].split('E');return {x:100*a[1],y:100*a[0]};" -m "delete c.grd_id" -a 10 -o ./out/demo_pop/1000m/ -e parquet -t 256
#gridtiler -i ./input/csv_Demographie_100m_Gitter/out_demo_pop.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a=c.grd_id.split('N')[1].split('E');return {x:100*a[1],y:100*a[0]};" -m "delete c.grd_id" -a 20 -o ./out/demo_pop/2000m/ -e parquet -t 256
#gridtiler -i ./input/csv_Demographie_100m_Gitter/out_demo_pop.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a=c.grd_id.split('N')[1].split('E');return {x:100*a[1],y:100*a[0]};" -m "delete c.grd_id" -a 50 -o ./out/demo_pop/5000m/ -e parquet -t 256
gridtiler -i ./input/csv_Demographie_100m_Gitter/out_demo_pop.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a=c.grd_id.split('N')[1].split('E');return {x:100*a[1],y:100*a[0]};" -m "delete c.grd_id" -a 100 -o ./out/demo_pop/10000m/ -e parquet -t 256
gridtiler -i ./input/csv_Demographie_100m_Gitter/out_demo_pop.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a=c.grd_id.split('N')[1].split('E');return {x:100*a[1],y:100*a[0]};" -m "delete c.grd_id" -a 200 -o ./out/demo_pop/20000m/ -e parquet -t 256
gridtiler -i ./input/csv_Demographie_100m_Gitter/out_demo_pop.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a=c.grd_id.split('N')[1].split('E');return {x:100*a[1],y:100*a[0]};" -m "delete c.grd_id" -a 500 -o ./out/demo_pop/50000m/ -e parquet -t 256

