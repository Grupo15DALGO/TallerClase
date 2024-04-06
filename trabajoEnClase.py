# Función para encontrar el conjunto de un elemento i
def encontrar(padre, i):
    if padre[i] == i:
        return i
    return encontrar(padre, padre[i])

# Función que une dos conjuntos en uno solo
def union(padre, rango, x, y):
    x_raiz = encontrar(padre, x)
    y_raiz = encontrar(padre, y)

    if rango[x_raiz] < rango[y_raiz]:
        padre[x_raiz] = y_raiz
    elif rango[x_raiz] > rango[y_raiz]:
        padre[y_raiz] = x_raiz
    else:
        padre[y_raiz] = x_raiz
        rango[x_raiz] += 1

# Función principal del algoritmo de Kruskal
def kruskal(vertices, aristas):
    resultado = []

    aristas = sorted(aristas, key=lambda item: item[2])

    padre = list(range(vertices + 1))
    rango = [0] * (vertices + 1)

    e = 0
    i = 0

    while e < vertices - 1 and i < len(aristas):  # Corregimos aquí
        u, v, w = aristas[i]
        i = i + 1
        x = encontrar(padre, u)
        y = encontrar(padre, v)

        if x != y:
            e = e + 1
            resultado.append((u, v, w))
            union(padre, rango, x, y)

    suma = 0
    for arista in resultado:
        suma += arista[2]
    return suma



def bfs(grafo, inicio, nodos_a_visitar):
    visitados = set()
    cola = [inicio]
    visitados.add(inicio)
    while cola:
        nodo = cola.pop(0)
        for arista in grafo:
            u, v, _ = arista
            if u == nodo:
                vecino = v
            elif v == nodo:
                vecino = u
            else:
                continue
            if vecino not in visitados:
                cola.append(vecino)
                visitados.add(vecino)
    nodos_no_visitados = [nodo for nodo in nodos_a_visitar if nodo not in visitados]
    return nodos_no_visitados



def aereopuertos(destinos, cost, lista_aristas):
    lista=[]
    for i in range(1,destinos+1):
        lista.append(i)

    desconectados=bfs(lista_aristas, lista_aristas[0][0], lista)
    costo=0
    num=0
    for location in desconectados:
        costo+=cost
        num+=1
    total=destinos-len(desconectados)
    costo+=kruskal(len(lista), lista_aristas)+cost

    return costo, num

ejemplo=[(12, 9, 44),(7, 10, 19),(1, 12, 24),(7, 3, 53),(4, 10, 43),(9, 12, 56),(3, 1, 45),(4, 7, 62)]

print(aereopuertos(12, 54, ejemplo))



