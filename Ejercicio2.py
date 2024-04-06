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

    padre = list(range(vertices))
    rango = [0] * vertices

    for arista in aristas:
        u, v, w = arista
        x = encontrar(padre, u)
        y = encontrar(padre, v)

        if x != y:
            resultado.append((u, v, w))
            union(padre, rango, x, y)

    return resultado

def main():
    with open('input2.txt', 'r') as f:
        T = int(f.readline().strip())
        for case in range(1, T + 1):
            n = int(f.readline().strip())
            graph = []
            for _ in range(n):
                row = list(map(int, f.readline().strip().split(", "))) 
                graph.append(row)
            

            aristas = []
            for i in range(n):
                for j in range(i + 1, n):
                    if graph[i][j] > 0:
                        aristas.append((i, j, graph[i][j]))

       
            mst = kruskal(n, aristas)

            print("Case {}:".format(case))
            for edge in mst:
                u, v, w = edge
                print("{}-{} {}".format(chr(u + 65), chr(v + 65), w))

if __name__ == "__main__":
    main()
