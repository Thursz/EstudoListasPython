# Constantes para facilitar a leitura do código
MATRICULA_INDEX = 0
NOME_INDEX = 1
NOTAS_INDEX_START = 2

# Função para informar notas dos alunos
def informarNotas(alunos, matricula, n1, n2, n3, n4):
    for aluno in alunos:
        if aluno[MATRICULA_INDEX] == matricula:
            # Adiciona as notas na lista do aluno
            notas = [n1, n2, n3, n4]
            aluno.extend(notas)
            return True
    # Se a matrícula não foi encontrada
    return False

# Lista de alunos
alunos = [[1, 'Art'], [2, 'Thrs'], [3, 'Ruthrs']]

# Exemplo de uso
matricula = 2
n1, n2, n3, n4 = 8, 7, 6, 9

if informarNotas(alunos, matricula, n1, n2, n3, n4):
    print("Notas atualizadas com sucesso!")
else:
    print("Matrícula não encontrada.")
print(alunos)

def pesquisarAluno(alunos,nome):
    indice = alunos.index(nome)
    return indice


nome = input('Digite o nome do aluno:')