'''
Here is a graph given by the adjacency list:
vertex adjacent vertices
 0      (1, 2, 3)
 1      (0, 2, 3)
 2      (0, 1, 3)
 3      (0, 1, 2, 5)
 4      (5, 6, 7)
 5      (3, 4, 6)
 6      (4, 5, 7)
 7      (4, 6)
'''

graph = {0:{1,2,3}, 1:{0,2,3}, 2:{0,1,3}, 3:{0,1,2,5}, 4:{5,6,7}, 5:{3,4,6}, 6:{4,5,7}, 7:{4,6}}

def bfs(graph, start_node, visited=set(), traversal_order=list()):
    queue=[]
    if start_node not in visited:
        traversal_order.append(start_node)
        visited.add(start_node)
        for nodes in graph[start_node]:
            traversal_order.append(nodes)
            queue.append(nodes)
            print(traversal_order)
    
    if len(visited) == graph.keys():
        return traversal_order
    if len(queue) != 0:
        for node in queue:
            bfs(graph, node, visited, traversal_order)

    return traversal_order

print(bfs(graph, 1))
