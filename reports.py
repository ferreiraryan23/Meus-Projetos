from core import inventario
def gerar_relatorio_categoria():
    '''Função para gerar relatório de itens por categoria'''
    
    if not inventario:
        print("O inventário está vazio.")
        return

    categorias = {}
    for item in inventario:
        cat = item['categoria']
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append(item)
    
    print("\n=== RELATÓRIO POR CATEGORIA ===")
    for categoria, itens in categorias.items():
        print(f"\n📂 CATEGORIA: {categoria.upper()}")
        print("-" * 30)
        for item in itens:
            # CORREÇÃO: Alterado de item['item'] para item['id']
            print(f"ID: {item['id']} | Nome: {item['nome']}")
            print(f"Quantidade: {item['quantidade']} | Preço: R${item['preco']}")
            print(f"Estado: {item['estado']} | Obs: {item['observacoes']}")
            print("-" * 15)