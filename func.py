def cadastrarAluno (alunos,matricula,nome):
    alunos.append([matricula,nome])
    return alunos

def imprimirAlunos (alunos):
    for aluno in alunos:
        print(f'{aluno[0]} - {aluno[1]}')

def informarNotas(alunos,matricula,n1,n2,n3,n4):
    for i in range(len(alunos)):
        if alunos[i][0] == matricula:
            notas = [n1,n2,n3,n4]
            alunos[i].extend(notas)
            return True
    return False

def pesquisarAluno(alunos,nome):
    for i in range(len(alunos)):
        if alunos[i][1] in nome:
            return nome
    return False


    
    
