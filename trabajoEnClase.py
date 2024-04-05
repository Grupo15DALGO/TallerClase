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

    padre = []
    rango = []

    for nodo in range(vertices):
        padre.append(nodo)
        rango.append(0)

    e = 0
    i = 0

    while e < vertices - 1:
        u, v, w = aristas[i]
        i = i + 1
        x = encontrar(padre, u)
        y = encontrar(padre, v)

        if x != y:
            e = e + 1
            resultado.append((u, v, w))
            union(padre, rango, x, y)

    suma=0
    for arista in resultado:
        suma+=arista[2]
    return(suma)




def construir_grafo(aristas):
    grafo = {}
    for u, v, peso in aristas:
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append((v, peso))
        grafo[v].append((u, peso))  # Añadir esta línea si el grafo es no dirigido
    return grafo

def bfs(grafo, inicio, nodos_a_visitar):
    visitados = set()
    cola = [inicio]
    visitados.add(inicio)
    while cola:
        nodo = cola.pop(0)
        for vecino, _ in grafo.get(nodo, []):
            if vecino not in visitados:
                cola.append(vecino)
                visitados.add(vecino)
    nodos_no_visitados = [nodo for nodo in nodos_a_visitar if nodo not in visitados]
    return nodos_no_visitados




def aereopuertos(destinos, cost, lista_aristas):
    lista=[]
    for i in range(destinos):
        lista.append(i)

    desconectados=bfs(lista_aristas, lista_aristas[0][0], lista)
    costo=0
    num=0
    for location in desconectados:
        lista_aristas.pop(location)
        costo+=cost
        num+=1
    total=destinos-len(desconectados)
    costo+=kruskal(total, lista_aristas)+cost

    return costo, num

ejemplo=[(12, 9, 44),(7, 10, 19),(1, 12, 24),(7, 3, 53),(4, 10, 43),(9, 12, 56),(3, 1, 45),(4, 7, 62)]

print(aereopuertos(12, 54, ejemplo))



