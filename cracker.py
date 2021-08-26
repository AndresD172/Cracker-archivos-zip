import os

dirc = os.path.abspath(__file__)
abspat = os.path.split(dirc)

try:
   pass_file = open(f"{abspat[0]}\\10-million-password-list-top-1000000.txt", "r")
except:
   print('No se pudo abrir el diccionario de claves')
   quit()

archivo = str(input('Ingrese la ruta del archivo: '))
extraccion = str(input('Ingrese la ruta de extracción: '))

for password in pass_file:
    password = password.replace("\n","")
    cmd = f"7z e {archivo} -o{extraccion} -p{password} -y" 
    print(cmd)

    os.system(cmd)

    


