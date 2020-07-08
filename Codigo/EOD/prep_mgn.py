#File :
#This file 

#Created by Lorenzo Aldeco on 07/08/20 14:20:40:
#Last modified by Lorenzo Aldeco on 07/08/20 14:20:40

import logging, pathlib, pandas

if __name__ == "__main__":
    
    runfile=pathlib.Path(__file__).absolute()
    rundir=runfile.parent
    
    logging.basicConfig(filename=str(rundir)+"/"+str(runfile.stem)+".txt",filemode='w',format='%(asctime)s:%(message)s',level=logging.DEBUG)
    logging.info("Starting "+str(runfile))
    
    #Read viajes csv
    viajes=pandas.read_csv('D:/Personal Directory/Lorenzo/Datos_GIS_ITAM/Clases/Encuestas/EOD_ZMVM/generated/viajes/viajes.csv')
    list(viajes.columns)
    
    #Create list of unique estado mun pairs
    ori_edo_str=viajes['ori_ent'].apply(str).str.zfill(2)
    ori_mun_str=viajes['ori_del'].apply(str).str.zfill(2)
    
    ori_idedomun=ori_edo_str.str.cat(ori_mun_str)
    
    des_edo_str=viajes['des_ent'].apply(str).str.zfill(2)
    des_mun_str=viajes['des_del'].apply(str).str.zfill(2)
    
    des_idedomun=des_edo_str.str.cat(des_mun_str)
    
    idedomun=ori_idedomun.append(des_idedomun).unique().tolist()
    
        
    logging.info("Done with "+str(runfile))