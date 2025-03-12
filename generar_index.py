import os
import json

# Ruta del archivo de datos en el disco D:
data_file_path = 'D:/Biblia/datos.txt'  # Asegúrate de que esta ruta es correcta

# Leer los datos desde el archivo
with open(data_file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Procesar los datos (este paso depende del formato de tus datos)
# Aquí asumimos que los datos están en formato JSON
data_dict = json.loads(data)

# Ruta del archivo index.json que se creará
output_file_path = 'D:/Biblia/index.json'

# Escribir los datos en el archivo index.json
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, indent=4)

print(f'Archivo index.json creado en {output_file_path}')
