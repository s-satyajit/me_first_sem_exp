from collections import defaultdict
import time

def map_coloring(graph, num_colors):
    nodes = list(graph.keys())
    coloring = {}
    domains = {node: set(range(num_colors)) for node in nodes}

    def is_valid(node, color):
        for nb in graph[node]:
            if nb in coloring and coloring[nb] == color:
                return False
        return True

    def forward_check(node, color):
        removed = []
        for nb in graph[node]:
            if nb not in coloring and color in domains[nb]:
                domains[nb].remove(color)
                removed.append((nb, color))
        return removed

    def restore(removed):
        for node, color in removed:
            domains[node].add(color)

    def select_unassigned():
        unassigned = [n for n in nodes if n not in coloring]
        if not unassigned:
            return None
        return min(unassigned, key=lambda n: len(domains[n]))

    def backtrack():
        node = select_unassigned()
        if node is None:
            return True
        for color in list(domains[node]):
            if is_valid(node, color):
                coloring[node] = color
                removed = forward_check(node, color)
                if backtrack():
                    return True
                del coloring[node]
                restore(removed)
        return False

    t0 = time.time()
    success = backtrack()
    t1 = time.time()
    print(f"Time taken: {(t1 - t0) * 1000:.3f} ms")
    return coloring if success else None


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["B", "C"]
    }
    num_colors = 3
    result = map_coloring(graph, num_colors)
    if result:
        print("Coloring found:", result)
    else:
        print("No valid coloring possible")
