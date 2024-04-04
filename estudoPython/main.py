from func import *

alunos = [[1, 'Art', [9, 8, 9, 9]], [2, 'Thrs', [6, 8, 9, 8]], [3, 'Ruthrs', [5, 6, 5, 6]]]

while True:

    menu = int(input('''Menu de opções
    1 = Cadastrar aluno
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
        nota1 = int(input('Digite a nota 1:'))
        nota2 = int(input('Digite a nota 2:'))
        nota3 = int(input('Digite a nota 3:'))
        nota4 = int(input('Digite a nota 4:'))
        
        informarNotas(alunos,matricula,nota1,nota2,nota3,nota4)
        print(alunos)
    
    elif menu == 4:
        nome = input('Digite o nome do aluno:')
        pesquisarAluno(alunos,nome)
    
    elif menu == 5:
        matricula = int(input('Digite a matricula do aluno:'))
        excluirAluno(alunos,matricula)   
        print(alunos)
        

    elif menu == 6:
        relatorioFinal(alunos)


    elif menu == 0:
        
        print('Saindo...')
        break
