from func import *

alunos = [[1,'Art'],[2,'Thrs'],[3,'Ruthrs']]

while True:

    menu = int(input('''Menu de opções
    1 = Cadastrar aluno
    2 = Imprimir alunos
    3 = Informar notas
    4 = Pesquisar aluno
    5 = Excluir aluno
    6 = Relatório final
    0 = sair
    Opção ==>'''))

    if menu == 1:

        matricula = int(input('Digite a matricula do aluno:'))
        nome = input('Digite o nome do aluno:')
        print(cadastrarAluno(alunos,matricula,nome))
        
    elif menu == 2:

        imprimirAlunos(alunos)
        
    elif menu == 3:

        matricula = int(input('Digite o número da matrícula:'))
        n1 = int(input('Digite a nota 1:'))
        n2 = int(input('Digite a nota 2:'))
        n3 = int(input('Digite a nota 3:'))
        n4 = int(input('Digite a nota 4:'))
        informarNotas(alunos,matricula,n1,n2,n3,n4)
        print(alunos)
    
    elif menu == 4:
        nome = input('Digite o nome do aluno:')
        print(pesquisarAluno(alunos,nome))


    elif menu == 0:
        
        print('Saindo...')
        break

