import shutil

nombre_archivo = 'fuentes.zip'
ruta_archivo = '/root/Data/'

shutil.unpack_archive(nombre_archivo, ruta_archivo)