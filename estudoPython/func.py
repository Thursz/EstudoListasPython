def cadastrarAluno (alunos,matricula,nome):
    alunos.append([matricula,nome])
    return alunos

def imprimirAlunos (alunos):
    for aluno in alunos:
        print(f'{aluno[0]} - {aluno[1]}')

def informarNotas(alunos,matricula,nota1,nota2,nota3,nota4):
    for i in range(len(alunos)):
        if alunos[i][0] == matricula:
            alunos[i].append([nota1,nota2,nota3,nota4])


def pesquisarAluno(alunos,nome):
    for aluno in alunos:
        media = CalcMedia(aluno[2])
        situacao = situationAluno(media)
        if nome in aluno[1]:
            print(f'Matricula? {aluno[0]}')
            print(f'Nome: {aluno[1]}')
            print(f'Notas: {aluno[2]}')
            print(f'Média: {media}')
            print(f'Situação: {situacao}')
    
def relatorioFinal(alunos):
    for aluno in alunos:
        media = CalcMedia(aluno[2])
        situacao = situationAluno(media)
        print(f'{aluno[0]} - {aluno[1]} | Média: {media} | {situacao}')

def situationAluno(media):
    if media >= 7:
        return 'Aprovado'
    else:
        return 'Reprovado'
    
def CalcMedia(notas):
    media = sum(notas)/len(notas)

    return media

def excluirAluno(alunos,matricula):
    for i in range(len(alunos)):
        if alunos[i][0] == matricula:
            alunos.pop(i)
            return 'Aluno excluído com sucesso!'
        
    return 'Matrícula inválida!'


