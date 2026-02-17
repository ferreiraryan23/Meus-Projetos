from core import inventario

def validar_por_id(id_item):
    """Verifica se um ID existe no inventário. Suporta ID como int ou string numérica."""
    try:
        id_item = int(id_item) #
    except ValueError:
        return False
        
    return any(item["id"] == id_item for item in inventario)

def validar_por_nome(nome):
    """Verifica se um nome (case-insensitive) já existe no inventário."""
    return any(item["nome"].lower() == nome.lower() for item in inventario)