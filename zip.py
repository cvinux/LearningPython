import shutil

nombre_archivo = '/root/Data/ejemplo/fuentes.zip'
ruta_archivo='/root/Data/'

shutil.unpack_archive(nombre_archivo,ruta_archivo)

print ("Descomprimir exitoso")