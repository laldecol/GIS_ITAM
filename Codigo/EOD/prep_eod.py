#File E:\Codes-Lorenzo\GIS_ITAM\Codigo\EOD\prep_eod.py:
#This file reads and prepares for analysis INEGI's origin destination survey

#Created by Lorenzo Aldeco on 07/06/20 18:38:14:
#Last modified by Lorenzo Aldeco on 07/06/20 18:38:14

import logging, pathlib, pandas, simpledbf, os
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

def dbf_to_csv(path):
    
    assert os.path.splitext(path)[1]=='.dbf'
    
    #Name output csv file same as input dbf
    [dirname,filename]=os.path.split(path)
    csv_file=dirname+os.path.splitext(filename)[0]+'.csv'
    
    #Read dbf object
    print('Reading '+path)
    dbf = simpledbf.Dbf5(path, codec='utf-8')
    
    #Write csv file
    if os.path.isfile(csv_file):
        os.remove(csv_file)
    
    print('Writing '+csv_file)
    dbf.to_csv(csv_file)
    
    return csv_file
def clean_viaje_df(df):
    var_dict={'P5_3':'dia_viaj',
              'P5_6':'ori_lug','P5_7_6':'ori_del','P5_7_7':'ori_ent', 'DTO_ORIGEN':'ori_dto',
              'P5_11A':'des_lug','P5_12_6':'des_del','P5_12_7':'des_ent', 'DTO_DEST':'des_dto',
              'P5_9_1':'ini_hor','P5_9_2':'ini_min','P5_10_1':'fin_hor','P5_10_2':'fin_min',
              'P5_14_01':'dummy_auto','P5_15_01':'num_auto',
              'P5_14_02':'dummy_micro','P5_15_02':'num_micro',
              'P5_14_03':'dummy_uber','P5_15_03':'num_uber',
              'P5_14_04':'dummy_taxi','P5_15_04':'num_taxi',
              'P5_14_05':'dummy_metro','P5_15_05':'num_metro',
              'P5_14_06':'dummy_rtp','P5_15_06':'num_rtp',
              'P5_14_07':'dummy_bici','P5_15_07':'num_bici',
              'P5_14_08':'dummy_bus','P5_15_08':'num_bus',
              'P5_14_09':'dummy_moto','P5_15_09':'num_moto',
              'P5_14_10':'dummy_trole','P5_15_10':'num_trole',
              'P5_14_11':'dummy_mbus','P5_15_11':'num_mbus',
              'P5_14_12':'dummy_tlig','P5_15_12':'num_tlig',
              'P5_14_13':'dummy_tsub','P5_15_13':'num_tsub',
              'P5_14_14':'dummy_camin','P5_15_14':'num_camin',
              'P5_14_15':'dummy_mcabl','P5_15_15':'num_mcabl',
              'P5_14_16':'dummy_bitax','P5_15_16':'num_bitax',
              'P5_14_17':'dummy_motax','P5_15_17':'num_motax',
              'P5_14_18':'dummy_tresc','P5_15_18':'num_tresc',
              'P5_14_19':'dummy_trper','P5_15_19':'num_trper',
              'P5_14_20':'dummy_otro','P5_15_20':'num_otro'}
    df.rename(columns=var_dict, inplace=True)
    df_ret=df[['ID_VIA','ID_SOC','dia_viaj','N_VIA',
               'ori_ent','ori_del','ori_dto','ori_lug',
               'des_ent','des_del','des_dto','des_lug',
               'ini_hor','ini_min',
               'fin_hor','fin_min',
               'FACTOR','SEXO','EDAD']]
    
    return df_ret
    
    
if __name__ == "__main__":
    
    runfile=pathlib.Path(__file__).absolute()
    rundir=runfile.parent
    
    filedir='D:/Personal Directory/Lorenzo/Datos_GIS_ITAM/Clases/Encuestas/bd_eod_2017_dbf/'
    dbf_viajes=filedir+'TVIAJE.dbf'
    csv_viajes=dbf_to_csv(dbf_viajes)
    
    viajes_cols=['ID_VIA','ID_SOC','N_VIA',
                 'P5_3', 'P5_6', 'P5_7_6', 'P5_7_7', 'DTO_ORIGEN', 'P5_11A', 'P5_12_6', 'P5_12_7', 
                 'DTO_DEST', 'P5_9_1', 'P5_9_2', 'P5_10_1', 'P5_10_2', 'P5_14_01', 'P5_15_01',
                 'P5_14_02', 'P5_15_02', 'P5_14_03', 'P5_15_03', 'P5_14_04', 'P5_15_04',
                 'P5_14_05', 'P5_15_05', 'P5_14_06', 'P5_15_06', 'P5_14_07', 'P5_15_07',
                 'P5_14_08', 'P5_15_08', 'P5_14_09', 'P5_15_09', 'P5_14_10', 'P5_15_10',
                 'P5_14_11', 'P5_15_11', 'P5_14_12', 'P5_15_12', 'P5_14_13', 'P5_15_13',
                 'P5_14_14', 'P5_15_14', 'P5_14_15', 'P5_15_15', 'P5_14_16', 'P5_15_16',
                 'P5_14_17', 'P5_15_17', 'P5_14_18', 'P5_15_18', 'P5_14_19', 'P5_15_19',
                 'P5_14_20', 'P5_15_20',
                 'SEXO', 'FACTOR', 'EDAD']
    
    print('Reading '+csv_viajes+' to dataframe.')
    df_viajes=pandas.read_csv(csv_viajes,usecols=viajes_cols)
    df_viajes=clean_viaje_df(df_viajes)
    
    list(df_viajes)
    
    df_viajes.head()
    
    logging.basicConfig(filename=str(rundir)+"/"+str(runfile.stem)+".txt",filemode='w',format=':',level=logging.DEBUG)
    logging.info("Starting "+str(runfile))
    
    logging.info("Done with "+str(runfile))