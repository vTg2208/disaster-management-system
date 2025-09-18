class MaxFlow:

    def bfs(self, source, sink, parent,graph):
        visited = set()
        queue = [source]
        visited.add(source)

        while queue:
            u = queue.pop(0)

            # Explore neighbors of u
            for v, capacity in graph.get(u, []):
                if v not in visited and capacity > 0:
                    parent[v] = u
                    visited.add(v)
                    if v == sink:
                        return True
                    queue.append(v)
        return False

    def ford_fulkerson(self, source, sink,graph):
        parent = {}
        max_flow = 0

        # Augment the flow while there is a path from source to sink
        while self.bfs(source, sink, parent,graph):
            # Find the maximum flow in the path found by BFS
            path_flow = float('inf')
            s = sink
            # finds the minimum weighted edge (min-cut)
            while s != source:
                for i, (neighbor, capacity) in enumerate(graph[parent[s]]):
                    if neighbor == s:
                        path_flow = min(path_flow, capacity) 
                        break
                s = parent[s]
            

            # Update capacities in the residual graph
            # update remaining weights as CW - MW
            v = sink
            while v != source:
                u = parent[v]
                for i, (neighbor, capacity) in enumerate(graph[u]):
                    if neighbor == v:
                        graph[u][i] = (neighbor, capacity - path_flow)
                        break
                graph[v].append((u, path_flow))
                v = parent[v]

            # add min edge to max flow
            max_flow += path_flow

        return max_flow