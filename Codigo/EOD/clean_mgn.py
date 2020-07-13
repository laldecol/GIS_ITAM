import pickle


id_file='D:/Personal Directory/Lorenzo/Datos_GIS_ITAM/Clases/Encuestas/EOD_ZMVM/generated/mun_ids.list'
with open(id_file, mode='rb') as file:
    id_list=pickle.load(file)

layer=iface.activeLayer()

fields=layer.fields()
for field in fields:
    print(field.name(), field.typeName())

print(len(list(layer.getFeatures())))
for f in layer.getFeatures():
    print(f['CVEGEO'])
    