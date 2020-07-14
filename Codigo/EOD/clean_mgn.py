import pickle


id_file='D:/Personal Directory/Lorenzo/Datos_GIS_ITAM/Clases/Encuestas/EOD_ZMVM/generated/mun_ids.list'
with open(id_file, mode='rb') as file:
    id_list=pickle.load(file)

layer=iface.activeLayer()

fields=layer.fields()
for field in fields:
    print(field.name(), field.typeName())

print(len(list(layer.getFeatures())))
select_ids=[]
for f in layer.getFeatures():
    if f['CVEGEO'] in id_list:
        select_ids.append(f.id())
    
_writer = QgsVectorFileWriter.writeAsVectorFormat(layer,"D:\Personal Directory\Lorenzo\Datos_GIS_ITAM\Clases\Encuestas\EOD_ZMVM\generated\muns_ZMVM.shp","utf-8", driverName = "ESRI Shapefile",onlySelected=True)