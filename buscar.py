from whoosh.index import open_dir
from whoosh.qparser import QueryParser

# Abrir el índice
ix = open_dir("indexdir")

# Crear un parser de consultas
parser = QueryParser("content", ix.schema)

# Función de búsqueda
def buscar(query_str):
    query = parser.parse(query_str)
    with ix.searcher() as searcher:
        results = searcher.search(query)
        for result in results:
            print(f"Título: {result['title']}, Ruta: {result['path']}")

# Solicitar al usuario la consulta de búsqueda
consulta = input("Introduce tu consulta de búsqueda: ")
buscar(consulta)
