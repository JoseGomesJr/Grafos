import shapely
import shapely.geometry
import re

import matplotlib.pyplot as plt
import geopandas as gpd

def lerVertices(arquivo):
  V = []

  numvertices = int(arquivo.readline())

  for vert in range( numvertices):
    vertices = re.findall("(^\d*/?.\d*), (\d*/?.\d*)",  arq.readline())
    #print(vertices[0])
    V.append([float(vertices[0][0]), float(vertices[0][1])])

  return V

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

p = gpd.GeoSeries(shapely_poly)
p.plot()
plt.show()
