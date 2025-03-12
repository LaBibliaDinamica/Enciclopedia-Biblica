import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser

# Definir el esquema para el índice
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)

# Crear el directorio para el índice si no existe
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

# Crear el índice
ix = create_in("indexdir", schema)

# Abrir el escritor de índice
writer = ix.writer()

# Recorrer los archivos en D:/Biblia/
for root, dirs, files in os.walk("D:/Biblia/"):
    for file in files:
        if file.endswith(".html") or file.endswith(".htm"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                writer.add_document(title=file, path=file_path, content=content)

# Cerrar el escritor de índice
writer.commit()
