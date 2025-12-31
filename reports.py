from core import  inventario

def gerar_relatorio_categoria():
    '''Função para gerar relatório de itens por categoria'''
    
    categorias = {}
    for item in inventario:
        categoria = item['categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    
    for categoria, itens in categorias.items():
        print(f"Categoria: {categoria}")
        for item in itens:
            print(f"""  ID: {item['item']} 
                  Nome: {item['nome']} 
                  Quantidade: {item['quantidade']} 
                  Preço: {item['preco']} 
                  Estado: {item['estado']}  
                  Observações: {item['observacoes']}"""
                  )
                  
        print('\n')