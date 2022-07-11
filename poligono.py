
import numpy as np
import shapely
import shapely.geometry
import re
import copy

num_vertices = int(0)


def lerVertices(arquivo):
    V = []
    global num_vertices
    numvertices = int(arquivo.readline())

    for vert in range(numvertices):
        vertices = re.findall("(^\d*/?.\d*), (\d*/?.\d*)",  arq.readline())
        # print(vertices[0])
        num_vertices += 1
        V.append([float(vertices[0][0]), float(vertices[0][1])])

    return V


def intersect_poligonons(line, poligons):

    for i in poligons:
        #print(line.intersection(i), line, i)
        intersec = line.intersection(i)
        if not intersec.is_empty:
            #print(intersec, line, i)
            if type(intersec) != shapely.geometry.Point:
                #print(line.intersection(i), line, i)
                return True
    return False


def montarGrafoVisibilidade(V):
    G = - np.ones((num_vertices, num_vertices))
    vert = int(-1)
    aux = 0
    poligons = []
    for j in V:
        poligons.append(shapely.geometry.Polygon(j))
    # print(poligons[1])
    for i in V:
        for j in i:
            vert += 1
            aux = 0
            for k in V:
                for v in k:
                    line = shapely.geometry.LineString([j, v])

                    if not intersect_poligonons(line, poligons):
                        print("-------not poligonons", line)
                        #print(vert, aux)
                        G[vert][aux] = 1
                    aux += 1

    return G


arq = open("mapa.txt", "r")
start_str = re.findall("(\d+)",  arq.readline())
start_int = [int(start_str[0]), int(start_str[1])]
print(start_int)
goal_str = re.findall("(\d+)",  arq.readline())
goal_int = [int(goal_str[0]), int(goal_str[1])]

print(goal_int)

obsaculos = int(arq.readline())
V = []

for obs in range(0, obsaculos):
    V.append(lerVertices(arq))

shapely_poly = shapely.geometry.Polygon(V[1])

print(shapely_poly)
print(V)
G = montarGrafoVisibilidade(V)
print(G)
