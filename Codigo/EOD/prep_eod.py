#File E:\Codes-Lorenzo\GIS_ITAM\Codigo\EOD\prep_eod.py:
#This file reads and prepares for analysis INEGI's origin destination survey

#Created by Lorenzo Aldeco on 07/06/20 18:38:14:
#Last modified by Lorenzo Aldeco on 07/06/20 18:38:14

import logging, pathlib, pandas
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from dbfread import DBF

def dbf_to_df(path):
    #Reads a .dbf file as a pandas DataFrame object
    dbf=DBF(path)
    frame = DataFrame(iter(dbf))
    return frame
    
if __name__ == "__main__":
    
    runfile=pathlib.Path(__file__).absolute()
    rundir=runfile.parent
    
    filedir='D:/Personal Directory/Lorenzo/Datos_GIS_ITAM/Clases/Encuestas/bd_eod_2017_dbf/'
    df_viajes=dbf_to_df(filedir+'TVIAJE.dbf')
    print(df_viajes.head())
    
    logging.basicConfig(filename=str(rundir)+"/"+str(runfile.stem)+".txt",filemode='w',format=':',level=logging.DEBUG)
    logging.info("Starting "+str(runfile))
    
    logging.info("Done with "+str(runfile))