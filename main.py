from dis import dis
from xmlrpc.client import Boolean, boolean
import numpy as np
import re

# grafo direcionado


def gerar_tabela_dist(G):

    dimensoes = re.findall("(\d+)\s+(\d+)",  G.readline())
    Grafo = - np.ones((int(dimensoes[0][0]), int(dimensoes[0][0])))
    for i in range(len(Grafo)):
        Grafo[i][i] = 0
    distancias = re.findall("(\d+)\s+(\d+)\s+(\d+)", G.read())
    for arestas in distancias:
        Grafo[int(arestas[0])-1][int(arestas[1])-1] = arestas[2]
    return Grafo
# grafo não direcionado


def gerar_tabela_dist_dir(G):
    dimensoes = re.findall("(\d+)\s+(\d+)",  G.readline())
    Grafo = - np.ones((int(dimensoes[0][0]), int(dimensoes[0][0])))
    for i in range(len(Grafo)):
        Grafo[i][i] = 0
    distancias = re.findall("(\d+)\s+(\d+)\s+(\d+)", G.read())
    for arestas in distancias:
        Grafo[int(arestas[0])-1][int(arestas[1])-1] = arestas[2]
        Grafo[int(arestas[1])-1][int(arestas[0])-1] = arestas[2]

    return Grafo


def dijkstra(D, origem):

    distancias = np.zeros(D.shape[0])
    for i in range(len(D)):
        distancias[i] = 9999
    visitados = np.zeros(D.shape[0])

    distancias[origem] = 0
    fila = []
    fila.append(origem)
    while len(fila) > 0:
        atual = fila.pop(0)
        if visitados[atual] != 1:

            visitados[atual] = 1

            for i in range(len(D)):
                v = i
                if D[atual][v] == -1:
                    continue
                custo = D[atual][v]

                if distancias[v] > distancias[atual] + custo:
                    distancias[v] = distancias[atual] + custo
                    fila.append(v)
    soma = 0
    for v in distancias:
        soma = soma+v
    maior = 0
    for v in distancias:
        if maior < v:
            maior = v
    return (soma, maior)


def central_dist(dists, max_dist_vec):
    central = 0
    menor = np.inf
    for v in range(len(dists)):
        if dists[v] < menor:
            menor = dists[v]
            central = v
        elif dists[v] == menor:
            if max_dist_vec[central] > max_dist_vec[v]:
                menor = dists[v]
                central = v
    return central


def dist_sum_vec(D):
    dist_vec = np.zeros(D.shape[0])
    # Faça o código aqui
    for i in range(len(D)):
        result = dijkstra(D, i)
        dist_vec[i] = result[0]
    #print(result[0])
    return dist_vec


def max_dist_vec(D):
    max_vec = np.zeros(D.shape[0])
  # Faça o código aqui
    for i in range(len(D)):
        result = dijkstra(D, i)
        max_vec[i] = result[1]
    return max_vec


G = open("grafo01.txt", "r")
i = int(input("Qual o tipo de grafo:\n1 - direcionado\n2 - não direcionado\n"))
if i == 1:
    D = gerar_tabela_dist(G)
elif i == 2:
    D = gerar_tabela_dist_dir(G)
print(D)

dist_vec = dist_sum_vec(D)
max_vec = max_dist_vec(D)

print(dist_vec)
print(max_vec)

central = central_dist(dist_vec, max_vec)

print("O central do grafo é:", central)
