#Realizamos la importación de la libreria con pip install PyMySQL
import pymysql


#Configuramos los datos de conexion con la base de datos
def obtener_conexion():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='app_crud_juego')