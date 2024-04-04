from functeste import *
palavras = ["python", "programação", "aleatório", "lista", "palavra", "exemplo"]
receba = palavras.copy()
print(receba)
listaPares = [1,5,23,4,56,7,8,9,12,3,4,67,44,34,22,65,33,77,9]
print(listaPares)
def pegarmeio (listaPares):
    meio = len(listaPares) //2
    if len(listaPares) %2 == 0:
        return listaPares[meio-1:meio+1]
    return listaPares[meio]
print(pegarmeio(listaPares))