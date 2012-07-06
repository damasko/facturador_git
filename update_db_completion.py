import sys, shelve
# devolvemos listado de completion_items
def completion_items():
    clientes_db = shelve.open("clientes.db")
    completion_items = clientes_db.keys()
    clientes_db.close()
    return completion_items
