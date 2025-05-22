# Se decompiló con PyLingual.

import json
import sys
jsonfile = sys.argv[1]
jsonkey = sys.argv[2] if len(sys.argv) > 2 else 'token1'
with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)
if jsonkey in obj:
    print(str(obj[jsonkey]))
else:
    print(f"Clave '{jsonkey}' no encontrada.")



# Recolectar información: El .pyc recupera una clave de un archivo JSON.

# Comprensión estática: Usa sys.argv[1] como archivo y accede a obj['token1'].

# Comprensión dinámica: Al ejecutarlo sin argumentos lanza IndexError. Con archivo válido, imprime "token1".

# Hipótesis: Sólo acepta el archivo como argumento, no permite elegir la clave.

# Pruebas: Cambiar la clave en el JSON no afecta la salida. Solo busca "token1".

# Validación: El comportamiento no cumple con lo descripto en la documentación.

# se verifica con el comando python getJason.py sitedata.json

# Diferencias con la documentación
# El código sólo permite recuperar la clave "token1".

# No acepta un segundo argumento para especificar otra clave.

# La documentación fue actualizada, pero el programa compilado no fue modificado.

# Esto se debe a una falta de mantenimiento del código fuente y cambios no implementados.