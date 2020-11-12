graph = {
    "x1": [("x2",10), ('x3',3)],
    'x2': [('x1',10)],
    'x3': [('x1',3),('x2',4),('x4',13)],
    'x4': [('x3',13)]
}

def find_shortest_path(graph, start, end, path=[]):
    print("starting", start, end)
    path = path + [start]
    if start == end:
        print("   returned 0")
        return path, 0
    if start not in graph:
        print("   returned None")
        return None, None
    shortest_path = None
    shortest_dist = None

    for node, dist in graph[start]:
        if node not in path:
            newpath, dist1 = find_shortest_path(graph, node, end, path)
            if newpath is not None:
                print("   going from",start,"to", node, dist, "+", dist1, "=", dist+dist1)
                dist1 += dist
                if not shortest_dist or dist1 < shortest_dist:
                    shortest_path = newpath
                    shortest_dist = dist1

    print("returning", shortest_path, shortest_dist, "if started from", start)
    return shortest_path, shortest_dist


print("Result", find_shortest_path(graph, 'x1', 'x2'))
