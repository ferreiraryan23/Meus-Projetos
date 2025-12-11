inventario = []
def cadastrar_item():
    '''Função para cadastrar um novo item no inventário.'''
    id_item = len(inventario) + 1
    nome = str(input("Digite o nome do item: "))
    quantidade = int(input("Digite a quantidade do item: "))
    preco = int((input("Digite o preço do item: ")))
    categoria = str(input("Digite a categoria do item: "))
    estado = str(input("Digite o estado do item (novo/usado): ")).lower()
    observacoes = str(input("Digite observações adicionais (ou deixe em branco): "))
    item = {
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco,
        'categoria': categoria,
        'estado': estado,
        'id': id_item,
        'observacoes': observacoes,
    }

    inventario.append(item)
    print("Item cadastrado com sucesso!")

def listar_itens():
    '''Função para listar todos os itens no inventário.'''
    if not inventario:
        print("Nenhum item cadastrado no inventário.")
        return
    for item in inventario:
        print(f'''ID: {item['id']} 
              Nome: {item['nome']} 
              Quantidade: {item['quantidade']}
              Preço: {item['preco']} 
              Categoria: {item['categoria']} 
              Estado: {item['estado']} 
              Observações: {item['observacoes']}''')

def buscar_por_nome_e_categoria(nome="", categoria=""):
    '''Função para buscar itens pela categoria ou pelo nome'''
    nome = input("Digite o nome : ").lower()
    categoria = input("Digite a categoria: ").lower()  
    
    resultados = [item for item in inventario
                  if categoria.lower() in item['categoria'].lower() or nome.lower() in item['nome'].lower()]
    
    if not resultados:
        print('Não há nenhum item com esses parametros de busca')
    else:
        for item in resultados:
            print(f'''ID: {item['id']} 
                  Nome: {item['nome']} 
                  Quantidade: {item['quantidade']} 
                  Preço: {item['preco']} 
                  Categoria: {item['categoria']} 
                  Estado: {item['estado']} 
                  Observações: {item['observacoes']}
                  ''')
        
def buscar_por_estado():
    "Função para buscar pelo estado"
    estado = input("Digite o estado do item desejado: ")
    resultados = [item for item in inventario 
                  if estado in item['estado'].lower()]

    if not resultados:
        print("Não há nenhum produto nesse estado")
    else:
        for item in resultados:
            print(f''' ID: {item['item']}
                Nome: {item['nome']} 
                  Quantidade: {item['quantidade']} 
                  Preço: {item['preco']} 
                  Categoria: {item['categoria']}
                  Estado: {item['estado']} 
                  Observações: {item['observacoes']}
                ''')
            
def add_or_remove():
    ''' Função para adicionar ou remover itens. '''

    id_item = int(input("Qual o id do item ?"))
    operacao = input("Deseja adicionar ou remover algum item? (add/rem): ").lower()
    quantidade = int(input("Quantas unidades desejas adicionar ou remover? "))

    for item in inventario:
        if item["id"] == id_item:
            if operacao == "add":
             item["quantidade"] += quantidade
             print(f'Quantidade adicionada. Total atualizado de "{item["nome"]}": {item["quantidade"]}')
        
            elif operacao == "rem":
                if item["quantidade"] >= quantidade:
                    item["quantidade"] -= quantidade
                    print(f'Quantidade removida. Total atualizado de "{item["nome"]}": {item["quantidade"]}')
   

def controle_de_stock():
    ''' Funçao para controle de ruptura de stock'''
    
    itens_criticos = []
    for item in inventario:
        if item["quantidade"] < 5:
            itens_criticos.append((item["nome"], item["quantidade"]))
    if itens_criticos:
        print('itens com quantidade critica: ')
        for item, quantidade in itens_criticos:
            print(f'- {item}: {quantidade} unidades ')
        else:
            print("Nenhum item com estoque critico. ")

def registo_de_emprestimos():
    ''' Função para registo de emprestimos de itens'''
    id_item = int(input("Qual o ID do item que desejas pegar emprestado? "))

    for item in inventario:
        if item["id"] == id_item:

            if item["quantidade"] > 0:
                item["quantidade"] -=1
                print(f'Empréstimo realizado com sucesso!')
                print(f'Item: {item["nome"]}')
                print(f'Quantidade restante no estoque: {item["quantidade"]}')
                    
            else:
                print("Este item está sem estoque no momento!")
                
        print("ID não encontrado no inventário.")

    

def total_by_cat(inventario):
    categorias = {}

    for item in inventario:   
        cat = item['categoria']
        categorias[cat] = categorias.get(cat, 0) + 1
        
    return categorias 

def valor_total():
    '''Função para calcular o valor total de itens no inventario'''

    total = 0
    for item in inventario:
        subtotal = item['preco'] * item['quantidade']
        total += subtotal
    return total

def report_itens_criticos():
    ''' funçao para listar os itens com quantidade baixa '''
    criticos = []

    for item in inventario:
        if item["quantidade"] < 5:
            criticos.append(item)

    if criticos:
        print('itens com quantidade critica: {Id}, {quantidade} ')
    else:
        print("Não ha itens em quantidade critica! ")