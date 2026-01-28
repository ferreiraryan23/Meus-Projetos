iinventario = []

def cadastrar_item():
    print("\n--- Cadastro de Item ---")
    id_item = len(inventario) + 1
    nome = str(input("Digite o nome do item: "))
    quantidade = int(input("Digite a quantidade do item: "))
    preco = float(input("Digite o preço do item: ")) 
    categoria = str(input("Digite a categoria do item: "))
    estado = str(input("Digite o estado do item (novo/usado): ")).lower()
    observacoes = str(input("Digite observações adicionais: "))
    
    item = {
        'id': id_item,
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco,
        'categoria': categoria,
        'estado': estado,
        'observacoes': observacoes,
    }

    inventario.append(item)
    print(f"Item '{nome}' cadastrado com sucesso com ID {id_item}!")

def listar_itens():
    print("\n--- Inventário Completo ---")
    if not inventario:
        print("Nenhum item cadastrado.")
        return
    for item in inventario:
        print(f"ID: {item['id']} | Nome: {item['nome']} | Qtd: {item['quantidade']} | Preço: R${item['preco']:.2f} | Cat: {item['categoria']}")

def buscar_por_nome_e_categoria():
    print("\n--- Busca ---")
    nome_busca = input("Digite o nome (ou deixe vazio): ").lower()
    cat_busca = input("Digite a categoria (ou deixe vazio): ").lower()
    
    resultados = [item for item in inventario
                  if (nome_busca in item['nome'].lower() if nome_busca else False) or 
                     (cat_busca in item['categoria'].lower() if cat_busca else False)]
    
    if not resultados:
        print('Nenhum item encontrado com esses parâmetros.')
    else:
        for item in resultados:
            print(f"ID: {item['id']} - Nome: {item['nome']} ({item['categoria']})")

def add_or_remove():
    try:
        id_item = int(input("Qual o ID do item? "))
        operacao = input("Deseja adicionar ou remover? (add/rem): ").lower()
        qtd_alterar = int(input("Quantidade: "))

        for item in inventario:
            if item["id"] == id_item:
                if operacao == "add":
                    item["quantidade"] += qtd_alterar
                    print(f"Novo total de {item['nome']}: {item['quantidade']}")
                elif operacao == "rem":
                    if item["quantidade"] >= qtd_alterar:
                        item["quantidade"] -= qtd_alterar
                        print(f"Novo total de {item['nome']}: {item['quantidade']}")
                    else:
                        print("Erro: Estoque insuficiente.")
                return
        print("ID não encontrado.")
    except ValueError:
        print("Erro: Digite valores numéricos válidos.")

def registo_de_emprestimos():
    try:
        id_item = int(input("Qual o ID do item para empréstimo? "))
        quantidade = int(input("Qual a quantidade desejada? "))

        for item in inventario:
            if item["id"] == id_item: 
                if quantidade > 0 and item["quantidade"] >= quantidade:
                    item["quantidade"] -= quantidade
                    print(f"Empréstimo de {quantidade}x {item['nome']} realizado!")
                    return
                else:
                    print("Quantidade indisponível ou inválida.")
                    return
        print("ID não encontrado.")
    except ValueError:
        print("Erro: Entrada inválida.")