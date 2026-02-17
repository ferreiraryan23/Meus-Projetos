def menu():
    while True:
        print("\n=== SISTEMA DE INVENTÁRIO ===")
        print("1. Cadastrar Item")
        print("2. Listar Itens")
        print("3. Buscar Item")
        print("4. Adicionar/Remover Estoque")
        print("5. Registrar Empréstimo")
        print("6. Ver Valor Total do Estoque")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            from core import cadastrar_item
            cadastrar_item()
        elif opcao =="2":
            from core import listar_itens
            listar_itens()
        elif opcao == "3":
            from core import buscar_item
            buscar_item()
        elif opcao == "4":
            from core import add_or_remove
            add_or_remove()
        elif opcao == "5":
            from core import registo_de_emprestimos
            registo_de_emprestimos()
        elif opcao == "6":
            from core import inventario
            print(f"Valor Total em Estoque: R${sum(i['preco'] * i['quantidade'] for i in inventario):.2f}")
        elif opcao == "0": break
        else: print("Opção inválida.")

if __name__ == "__main__":
    menu()