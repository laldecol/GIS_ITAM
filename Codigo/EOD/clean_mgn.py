
import pickle

from qgis.core import *

# Supply path to qgis install location
QgsApplication.setPrefixPath("/path/to/qgis/installation", True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

# Write your code here to load some layers, use processing
# algorithms, etc.

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory

id_file='D:/Personal Directory/Lorenzo/Datos_GIS_ITAM/Clases/Encuestas/EOD_ZMVM/generated/mun_ids.list'
prefix_path='C:/Program Files/QGIS 3.14/apps/qgis'
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

qgs.exitQgis()