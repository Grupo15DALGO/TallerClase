def encontrar(padre, i):
    if padre[i] == i:
        return i
    return encontrar(padre, padre[i])

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

def kruskal(vertices, aristas):
    resultado = []

    aristas = sorted(aristas, key=lambda item: item[2])

    padre = list(range(vertices + 1))
    rango = [0] * (vertices + 1)

    e = 0
    i = 0

    while e < vertices - 1 and i < len(aristas):
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
    return suma, len(resultado)

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
    costo_tree, num_airports = kruskal(len(lista), lista_aristas)
    costo += costo_tree + cost
    return costo, num

def main():
    with open('input.txt', 'r') as f:
        t = int(f.readline().strip())
        for case in range(1, t + 1):
            n, m, a = map(int, f.readline().strip().split())
            aristas = [tuple(map(int, f.readline().strip().split())) for _ in range(m)]
            costo, num_airports = aereopuertos(n, a, aristas)
            print("Case #{}: {} {}".format(case, costo, num_airports))

if __name__ == "__main__":
    main()
