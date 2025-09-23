import heapq
import math

def reconstruct(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return list(reversed(path))

def a_star(graph, start, goal, h=lambda u, v: 0):
    openq = [(h(start, goal), start)]
    g = {start: 0}
    parent = {}
    closed = set()

    while openq:
        f, u = heapq.heappop(openq)
        if u in closed:
            continue
        if u == goal:
            return reconstruct(parent, start, goal), g[goal]
        closed.add(u)
        for v, cost in graph.get(u, []):
            tentative = g[u] + cost
            if tentative < g.get(v, float('inf')):
                g[v] = tentative
                parent[v] = u
                heapq.heappush(openq, (tentative + h(v, goal), v))
    return None, float('inf')


if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }

    path, cost = a_star(graph, 'A', 'D', h=lambda u, v: 0)
    if path:
        print("A* (h=0) found:", path, "cost =", cost)
    else:
        print("A* (h=0) found no path")

    coords = {'A': (0,0), 'B': (1,0), 'C': (2,0), 'D': (3,0)}
    def euclid(u, v):
        (x1, y1) = coords[u]; (x2, y2) = coords[v]
        return math.hypot(x1 - x2, y1 - y2)

    path2, cost2 = a_star(graph, 'A', 'D', h=euclid)
    if path2:
        print("A* (Euclidean h) found:", path2, "cost =", cost2)
    else:
        print("A* (Euclidean h) found no path")
