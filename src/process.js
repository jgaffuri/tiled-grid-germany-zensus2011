#!/usr/bin/env node


//See https://observablehq.com/d/62acd402b96476b9
//https://uwdata.github.io/arquero/api/

//import {aq, op} from "arquero"
const aq = require("arquero");

console.log("Hallo welt !")
console.log(aq.loadCSV)

const dt = aq.loadCSV('./input/csv_Demographie_100m_Gitter/Bevoelkerung100M.csv');
//2GB limit exceeded !!!
