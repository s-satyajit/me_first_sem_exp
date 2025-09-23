while open not empty:
current = open.pop_min() # node with smallest f
if current == goal:
return reconstruct_path(parent, current), g[goal]
closed.add(current)
for neighbor in neighbors(current):
tentative_g = g[current] + cost(current, neighbor)
if neighbor in closed and tentative_g >= g.get(neighbor, inf):
continue
if tentative_g < g.get(neighbor, inf):
parent[neighbor] = current
g[neighbor] = tentative_g
f = tentative_g + h(neighbor)
open.insert_or_decrease_key(neighbor, f)
return failure