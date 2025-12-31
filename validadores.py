from core import inventario

def validar_por_id(id_item):
    for item in inventario:
        if item["id"] == id_item:
            return True
    return False    

def validar_por_nome(nome):
    for item in inventario:
        if item["nome"].lower() == nome.lower():
            return True
    return False
