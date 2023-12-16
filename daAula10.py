while True:
    def function_empresa():
        Empresa = {}
        while True:

            print('''            --------/ Bem-Vindo a Empresa /--------
            1- Adicionar empresa e descrião
            2- Renomear Empresa
            3- Renomear descrição da empresa
            4- Remover empresa
            5- listar empresa e descrição
            6- Sair''')

            op = int(input('digite a opção :'))

            # ------------------------- ADICIONANDO EMPRESA E DESCRIÇÃO --------------------------------

            if op == 1:
                nome = input(f'Escreva o nome da Empresa:')
                if nome not in Empresa:
                    Empresa[nome] = input(f'Agora escreva a descrição da {nome}:')
                    print(f'Empresa {nome} Adicionada com Sucesso!')
                else:
                    print(f'A empresa {nome} já existe!')



    # -------------------------  Renomear Empresa -----------------------------------

            elif op == 2:
                nome = input('Escreva a empresa:')
                if nome in Empresa:
                    nova_empresa = input(f'Escreva o novo nome de empresa {nome}:')
                    Empresa[nova_empresa] = Empresa.pop(nome)
                    print(f'Empresa renomeada com sucesso!')
                else:
                    print(f'A empresa {nome} já existe!')

    # -------------------------- Renomear Descrição Empresa --------------------------

            elif op == 3:
                nome = input('Escreva a Empresa que seja editar a descrição:')
                if nome in Empresa:
                    Empresa[nome] = input(f'Escreva a nova descrição da {nome}:')
                    print('Descrição editada com sucesso!')
                else:
                    print(f'A empresa {nome} já existe!')


            # ------------------------ Remover Empresa ---------------------------------------

            elif op == 4:
                nome = input('Escreva a empresa que deseja remover:')
                if nome in Empresa:
                    print(f'Tem certeza que voçê quer remover a empresa {nome}?')
                    op = input(f'Se a opção for SIM, digite (Y) se NÃO, (N)')
                    if op == 'N' or op == 'n':
                        print(f'Voçê desistiu de remover a empresa {nome}.')
                    elif op == 'Y' or op == 'y':
                        del Empresa[nome]
                        print(f'Empresa {nome} Removida com sucesso!')
                    else:
                        print('Opção invalida!')
                else:
                    print(f'A empresa {nome} não existe!')

            # ---------------- LISTAR EMPRESA E DESCRIÇÃO -------------------------------

            elif op == 5:
                for i in Empresa:
                    print(f'{i}:{Empresa[i]}')

            # ----------------------------- SAIR --------------------------------------------
            elif op == 6:
                print('Voçê saiu!')
                break

            else:
                print('Opção invalida!')


    '''//////////////////////////// FIM DA FUNÇÃO EMPRESAS //////////////////////////////////////'''


    def function_tarefas():
        tarefas = {}
        while True:
            print('''            --------/ Bem-Vindo a Empresa /--------
                1- Adicionar tarefa e descrião
                2- Listar tarefas e descrição
                3- Renomear tarefa
                4- Renomear descrição da tarefa
                5- Remover tarefa
                6- Sair''')

            op = input('Digite a opção :')

            # ------------------------- ADICIONANDO TAREFA E DESCRIÇÃO --------------------------------

            if op == 0:
                nome = input('Adicione a tarefa:')
                if nome not in tarefas:
                    tarefas[nome] = input(f'Agora escreva a descrição de {nome}:')
                    print('tarefa Adicionada com sucesso!')
                else:
                    print(f'A tarefa {nome}, já existe!')



            # ------------------------------- LISTAR TAREFAS E SUAS DESCRIÇÃO  ---------------------------

            elif op == 2:
                for k in tarefas:
                    print(f'{k}: {tarefas[k]}')

            # ----------------------------- Renomear tarefa ----------------------------------------------
            elif op == 3:

                tarefa_antiga = input('digite a tarefa antiga:')
                if tarefa_antiga in tarefas:
                    tarefa_nova = input('digite a tarefa nova:')
                    tarefas[tarefa_nova] = tarefas.pop(tarefa_antiga)
                    print(f"A tarefa {tarefa_antiga} foi renomeada para {tarefa_nova}.")
                else:
                    print(f"A tarefa {tarefa_antiga} não foi encontrada.")


            # -------------------------  Renomear descrição tarefa  --------------------------------

            elif op == 4:
                tarefa = input('De qual tarefa deseja Editar a descrição?')
                if tarefa in tarefas:
                    tarefas[tarefa] = input('Digite a nova Descrição:')
                    print(f'Descrição {tarefa} renomeada com Sucesso!')
                else:
                    print(f"A tarefa {tarefa} não foi encontrada.")

            # ------------------------ Remover tarefa ---------------------------------------

            elif op == 5:
                tarefa = input('Qual tarefa deseja Remover?')
                if tarefa in tarefas:
                    print(f'Tem certeza que quer remover {tarefa}?')
                    op = input('Se SIM, digite (Y) se NÃO, digite (N):')
                    if op == 'Y' or op == 'y':
                        del tarefas[tarefa]
                        print(f'Tarefa {tarefa} deletada com sucesso!')
                    elif op == 'N' or op == 'n':
                        print(f'Voçê desistiu de remover tarefa {tarefa}.')
                    else:
                        print('Opção invalida!')
                else:
                    print(f"A tarefa {tarefa} não foi encontrada.")

            # ----------------------------- SAIR --------------------------------------------
            elif op == 6:
                print('Voçê saiu!')
                break

            else:
                print('Opção invalida!')


    '''//////////////////////////////// FIM DA FUNÇÃO TAREFAS //////////////////////////////////'''

    print(''' ... PARA ENTRAR NO MENU ... 
        1- EMPRESAS
        2- TAREFAS 
        3- SAIR DO PROGRAMA''')

    opcao = input('Digite a opção (1) ou (2):')

    if opcao == '1':
        print(function_empresa())
    elif opcao == '2':
        print(function_tarefas())
    elif opcao == '3':
        print('Voçê saiu do programa!')
        break
    else:
        print('Opção invalida!')


