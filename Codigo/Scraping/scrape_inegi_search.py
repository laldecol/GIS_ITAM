#File E:\Codes-Lorenzo\GIS_ITAM\Codigo\Scraping\scrape_inegi_search.py:
#This file downloads all files matching given criteria from a search on INEGI's GIS database.

#Created by Lorenzo Aldeco on 06/08/20 16:18:01:
#Last modified by Lorenzo Aldeco on 06/08/20 16:18:01

import logging, pathlib, pandas, requests_html, re, wget

pandas.set_option('display.max_columns', None)

def downloader(inegi_csv,folder):
    """This prorgram reads a csv generated by INEGI's GIS data search, and downloads all files in it to the target folder"""
    df=pandas.read_csv(inegi_csv,
                       na_values=[""],
                       usecols=["upc", "titulo","formatos","escala","url"])
    
    df=df[df['formatos'].str.contains('grid')]
    urls=["https://www.inegi.org.mx/"+str(url) for url in df['url'].to_list()]
    session=requests_html.HTMLSession()
    
    rexp=re.compile(".*gr.zip*")
    
    for url in urls:
        r=session.get(url)
        r.html.render()
        links=list(filter(rexp.match,r.html.absolute_links))
        
        try:
            logging.info("Downloading %s", links[0])          
            wget.download(links[0],folder)
        except Exception as e:
            logging.info("Download of %s failed.", links)
            
    logging.info("Done running downloader")

if __name__ == "__main__":
    
    runfile=pathlib.Path(__file__).absolute()
    rundir=runfile.parent
    
    logging.basicConfig(filename=str(rundir)+"/"+str(runfile.stem)+".log",filemode='w',format='%(levelname)s:%(message)s',level=logging.DEBUG)
    logging.info("Starting "+str(runfile))
    
    inegi_csv="D:\Personal Directory\Lorenzo\Datos_GIS_ITAM\Clases\Rasters\INEGI_CSV\Mapas_2020-6-8_15-21-27.csv"
    folder="D:\Personal Directory\Lorenzo\Datos_GIS_ITAM\Clases\Rasters\Datos\csv_dump"
    downloader(inegi_csv, folder)
    
    logging.info("Done with "+str(runfile))