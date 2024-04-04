import random
alunos = [[1,'Art', [8, 8, 8, 8]], [2, 'Thrs', [6, 8, 9, 8]], [3, 'Ruthrs', [5, 6, 5, 6]]]
print(alunos)
novoaluno = [[4,'Vivi',[10,10,10,10]]]
print(novoaluno)
alunos.extend(novoaluno)
print(alunos)
print(novoaluno)
alunos[3][1] = 'Evelyn'
print(alunos)
listanova = [1,2,3,4,5,4,9,0]
indice = listanova.index(9)
print(indice)
conta = sum(listanova) / len(listanova)
print(conta)
print(listanova)
listanova.sort()
print(listanova)
nova = alunos[::-1]
print(nova)