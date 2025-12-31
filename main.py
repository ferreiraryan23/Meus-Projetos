def main(): 
    print("====== Bem-vindo ao Sistema de Inventário! ======")

    while True:
        print('\n Selecione uma opção: ')
        print('1. Cadastrar novo item ')
        print('2. Listar itens ')
        print('3. Buscar item por nome ou categoria ')
        print('4. Buscar item por estado de uso')
        print('5. Adicionar ou remover item ')
        print('6. Controle de stock ')
        print('7. Resgistar um emprestimo ')
        print('8. Total por categoria ')
        print('9. Valor total do inventario ')
        print('10. Report de itens criticos')
        print('11. Gerar um relatorio por categoria ')
        print('12. Sair ')

        escolha = input('Digite o numero da opção que desejas. ')

        if escolha == '1':
            from core import cadastrar_item
            cadastrar_item()
        elif escolha == '2':
            from core import listar_itens
            listar_itens()
        elif escolha == '3':
            from core import buscar_por_nome_e_categoria
            buscar_por_nome_e_categoria()
        elif escolha == '4':
            from core import buscar_por_estado
            buscar_por_estado()
        elif escolha == '5':
            from core import add_or_remove
            add_or_remove()
        elif escolha == '6':
            from core import controle_de_stock
            controle_de_stock()
        elif escolha == '7':
            from core import registo_de_emprestimos
            registo_de_emprestimos()
        elif escolha == '8':
            from core import total_by_cat
            total_by_cat()
        elif escolha == '9':
            from core import valor_total
            valor_total()
        elif escolha == '10':
            from core import report_itens_criticos
            report_itens_criticos()
        elif escolha == '11':
            from reports import gerar_relatorio_categoria
            gerar_relatorio_categoria()
        elif escolha == '12':
            print('Até logo.... ')
if __name__ == '__main__':
    main()