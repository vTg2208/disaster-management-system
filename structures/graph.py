import heapq
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_city(self, city):
        if city not in self.adj_list:
            self.adj_list[city] = []

    def remove_city(self, city):
    # Check if the vertex exists in the adjacency list
        if city in self.adj_list:
            # First, remove all edges associated with this vertex using remove_route
            for neighbor, _ in self.adj_list[city]:
                self.remove_route(neighbor, city)
            
            # Now remove the vertex itself from the adjacency list
            self.adj_list.pop(city)


    def add_route(self, city1, city2, distance):
        self.add_city(city1)
        self.add_city(city2)

        self.adj_list[city1].append((city2, distance))
        self.adj_list[city2].append((city1, distance))

    def remove_route(self, city1, city2):
        if city1 in self.adj_list and city2 in self.adj_list:
            # Remove city2 from city1's adjacency list
            self.adj_list[city1] = [(c, d) for c, d in self.adj_list[city1] if c != city2]
            
            # Remove city1 from city2's adjacency list
            self.adj_list[city2] = [(c, d) for c, d in self.adj_list[city2] if c != city1]
    
    def dfs(self, start, visited):
        # Mark the current node as visited
        visited.add(start)
        print(start)  # Process the node (e.g., print it)

        # Recur for all the vertices adjacent to this vertex
        for neighbor, weight in self.adj_list.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)


        
    def shortest_path(self, start, end):
    # Implements Dijkstra's algorithm to find the shortest path from start to end

        distances = {city: float('inf') for city in self.adj_list}  # Distance dictionary initialized to infinity
        distances[start] = 0  # Distance from start to itself is zero

        PQ = []  # Priority queue for Dijkstra's
        visited = set()  # Keeps track of visited nodes
        heapq.heappush(PQ, (0, start))  # Pushes start onto the priority queue with distance zero

        while PQ:
            # Pops node with the smallest distance
            current_distance, current_city = heapq.heappop(PQ)

            if current_city == end:  # Early stop if destination is reached
                break

            if current_city not in visited:
                visited.add(current_city)  # Marks current node as visited

                # Checks all adjacent vertices
                for neighbor, weight in self.adj_list[current_city]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        # Updates distance if a shorter path is found
                        distances[neighbor] = distance
                        heapq.heappush(PQ, (distances[neighbor], neighbor))  # Adds updated distance to priority queue

        # Calls function to backtrack and find the shortest path
        self.paths(start, end, set(), [], 0, distances[end])
        return distances[end] if distances[end] != float('inf') else -1

    def paths(self, src, dest, visited, curr_path, curr_dist, shortest_dist):
        # Recursive function to find and print the shortest path
        visited.add(src)  # Adds current location to visited set
        curr_path.append(src)  # Adds current location to the current path

        if src == dest:
            # If destination is reached and matches shortest time, print the path
            if curr_dist == shortest_dist:
                print("The shortest path  : ",curr_path)

            visited.remove(src)  # Backtrack
            curr_path.pop()
            return

        # Explore adjacent vertices
        for neighbor, weight in self.adj_list[src]:
            if neighbor not in visited:
                # Continues recursion with current path and accumulated dist
                self.paths(neighbor, dest, visited, curr_path, curr_dist + weight, shortest_dist)

        # Backtracking to explore other possible paths
        visited.remove(src)
        curr_path.pop()


    def prim_mst(self):
        # Implements Prim's algorithm to find the Minimum Spanning Tree (MST) starting from the first vertex in the adjacency list

        mst_edges = []  # List to stor e edges of the MST
        visited = set()  # Set to track visited nodes
        min_heap = []  # Min-heap for managing edges
        total_cost = 0  # Total cost of the MST

        # Get the first vertex from the adjacency list directly
        start = list(self.adj_list.keys())[0]  # Get the first key in the adjacency list
        visited.add(start)

        # Push initial edges from the start vertex to the heap 
        for neighbor, weight in self.adj_list[start]:
            heapq.heappush(min_heap, (weight, start, neighbor))  # (weight, src, dest)

        while min_heap:
            # Pops the edge with the smallest weight
            weight, src, to_vertex = heapq.heappop(min_heap)

            if to_vertex not in visited:
                # If the vertex has not been visited, add it to the MST
                visited.add(to_vertex)
                mst_edges.append((src, to_vertex, weight))  # Store the edge
                total_cost += weight  # Update the total cost

                # Add all edges from the newly added vertex to the heap
                for neighbor, edge_weight in self.adj_list[to_vertex]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (edge_weight, to_vertex, neighbor))  # Push neighbors into the heap

        # Output the edges in the MST and the total cost
        print("Edges in the Minimum Spanning Tree:")
        for from_vertex, to_vertex, weight in mst_edges:
            print(f"{from_vertex} -- {to_vertex} (weight: {weight})")
        print("Total cost of MST:", total_cost)





