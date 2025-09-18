# Disaster Response System

A comprehensive disaster management system implemented in Python using multiple data structures and algorithms to efficiently handle emergency response operations. The system is designed with a modular architecture where each data structure is implemented in separate files for better maintainability.

## Project Structure

```
disaster-response-system/
├── structures/
│   ├── avl_tree.py          # AVL Tree implementation for disaster severity management
│   ├── bst.py               # Binary Search Tree for historical data storage
│   ├── disjoint_set.py      # Union-Find for connected city components
│   ├── graph.py             # Graph implementation for city networks
│   ├── hash_map.py          # Custom HashMap for contacts and resources
│   ├── max_flow.py          # Ford-Fulkerson algorithm implementation
│   ├── max_heap.py          # Max heap for emergency prioritization
│   ├── min_heap.py          # Min heap for priority queue operations
│   └── trie.py              # Trie for efficient location search
├── about.txt                # Detailed function documentation
├── disaster_response_system.py  # Main system integration
├── main.py                  # Entry point for the application
├── README.md                # Project documentation
└── time_complexity          # Algorithm complexity analysis
```

## Features

### Core Data Structures (Modularized)
- **AVL Tree** (`avl_tree.py`): Self-balancing tree for disaster types organized by severity
- **Binary Search Tree** (`bst.py`): Historical response data storage and retrieval
- **Disjoint Set** (`disjoint_set.py`): Union-Find operations for connected city components
- **Graph** (`graph.py`): Network of cities and routes using adjacency lists
- **HashMap** (`hash_map.py`): Custom implementation for emergency contacts and resources
- **Max Flow** (`max_flow.py`): Ford-Fulkerson algorithm for resource distribution
- **Max Heap** (`max_heap.py`): Priority queue for high-urgency emergencies
- **Min Heap** (`min_heap.py`): Priority queue for low-urgency operations
- **Trie** (`trie.py`): Efficient location search and storage

### Key Algorithms
- **Dijkstra's Algorithm**: Shortest path calculation between cities
- **Prim's Algorithm**: Minimum spanning tree for optimal connectivity
- **Ford-Fulkerson**: Maximum flow algorithm for resource distribution
- **DFS Traversal**: City network exploration
- **AVL Rotations**: Self-balancing tree operations

## System Capabilities

### Network Management
- Add cities and routes with distances
- Remove cities and routes dynamically
- Find shortest paths between locations
- Calculate minimal cost travel networks
- Determine maximum resource flow capacity

### Emergency Operations
- Priority-based emergency queue management (Max/Min Heap)
- Disaster classification by severity levels (AVL Tree)
- Quick location search and verification (Trie)
- Historical response data tracking (BST)
- Emergency contact management per city (HashMap)

### Resource Management
- Resource inventory tracking for each city
- Optimal resource distribution planning
- Minimal cost resource network design
- Capacity planning for emergency supplies
- Connected component analysis (Disjoint Set)

## Installation & Usage

### Prerequisites
```python
import heapq
import copy
```

### Running the System
```bash
# Run the main application
python main.py

# Or run the integrated system directly
python disaster_response_system.py
```

## Menu-Driven Interface

The system provides 19 comprehensive operations:

### Network Operations (1-3, 6, 10-11)
1. **Add City and Route** - Create network connections
2. **Insert Disaster with Severity** - Classify disaster types using AVL Tree
3. **Search Location** - Find registered locations using Trie
6. **Find Shortest Path** - Calculate optimal routes using Dijkstra's
10. **Minimal Cost Travel** - Generate MST using Prim's algorithm
11. **Travel Cities** - DFS traversal of city network

### Emergency Management (4-5, 7-9)
4. **Add Emergency with Urgency** - Queue emergency requests in Max Heap
5. **Insert Historical Response Data** - Store in BST
7. **Display Top Priority Emergency** - View highest urgency case
8. **Display All Emergencies** - Show complete emergency queue
9. **Search Historical Response** - BST-based retrieval

### Resource Operations (12, 14-19)
12. **Max Flow Between Cities** - Calculate maximum resource flow
13. **Display Disasters** - Show disaster types by severity (AVL Tree)
14. **Add Resources** - Define resource routes between cities
15. **Minimal Resources** - Optimize resource distribution network
16. **Add Emergency Contacts** - Store emergency numbers using HashMap
17. **View Emergency Contacts** - Retrieve contact information
18. **Add/Update Resource Inventory** - Manage city resources
19. **Check Resource Availability** - View available resources

## Technical Implementation

### Modular Architecture Benefits
- **Separation of Concerns**: Each data structure is independently implemented
- **Code Reusability**: Individual modules can be imported and used elsewhere
- **Easy Testing**: Unit tests can be written for each module
- **Maintainability**: Bug fixes and enhancements are isolated to specific modules
- **Scalability**: New data structures can be added without affecting existing code

### Time Complexity Analysis
Detailed complexity analysis is available in the `time_complexity` file:
- **Graph Operations**: O(V + E) for DFS, O((V + E) log V) for Dijkstra's
- **AVL Tree**: O(log n) for insertion, deletion, and search
- **Heap Operations**: O(log n) for insertion and extraction
- **Trie Operations**: O(m) where m is the length of the string
- **HashMap Operations**: O(1) average case for insertion and retrieval

### Memory Efficiency
- **Graph**: O(V + E) space complexity
- **Trees**: O(n) space for n nodes
- **Heaps**: O(n) space for n elements
- **Trie**: O(ALPHABET_SIZE * N * M) where N is number of keys and M is average length

## Data Flow Architecture

1. **Initialization**: Load individual data structure modules
2. **Network Setup**: Cities and routes are added using Graph module
3. **Emergency Registration**: Disasters queued using Heap modules, classified using AVL Tree
4. **Resource Planning**: HashMap manages resources, Max Flow calculates distribution
5. **Response Optimization**: Graph algorithms calculate optimal paths
6. **Historical Tracking**: BST stores and retrieves response data
7. **Location Services**: Trie provides fast location lookup

## Example Workflow

```python
# Initialize system with modular components
system = DisasterResponseSystem()

# Network setup
system.add_city_and_route()  # Mumbai -> Delhi (500 km)

# Emergency management
system.add_emergency_with_urgency()  # Flood in Mumbai (urgency: 9)
system.insert_disaster_type_with_severity()  # Flood (severity: 8)

# Resource optimization
system.find_shortest_path_between_cities()  # Mumbai -> Delhi
system.max_flow()  # Calculate resource flow capacity

# Data retrieval
system.search_location()  # Quick location lookup
system.get_emergency_contacts()  # Retrieve emergency numbers
```

## Technical Specifications

- **Language**: Python 3.x
- **Architecture**: Modular, Object-Oriented Design
- **Memory Management**: Efficient data structure implementations
- **Algorithms**: Industry-standard graph and tree algorithms
- **Scalability**: Designed for large-scale disaster response networks

This modular disaster response system combines theoretical computer science concepts with practical emergency management requirements, providing a robust and maintainable solution for disaster response operations.

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/92077432/b1828d89-4d66-45e8-8078-6b88594c880d/image.jpg?AWSAccessKeyId=ASIA2F3EMEYESIHLI45J&Signature=Cumglrm7U1HUfAYxNRtNByeaSA4%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEEQaCXVzLWVhc3QtMSJHMEUCIQC0di6ChnRPcuAzEiVeD9FdnDOrwaXShKQnBLjhYpClcgIgDDHDCzlXL7e6MqWV9wOyvlfYQecbeNB4C1aHv%2Fl7Zkkq%2BgQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgw2OTk3NTMzMDk3MDUiDOoMCgcIujcYyTxfCSrOBKifd3JP81AQvhbWBNQa2Nnk2Mpml8joLq%2FtNQ3iE56Ix2d7WzYc6t35JZL8iLBSWVvhngqNIhVOmVJkuR%2FUOikyTZStZ62ZSRJux86UHFCqwrL8jqR3v5sDVoPGX3a5dt98iKGoO%2Fw4%2B598xdZpA4oHogw0DbGQmZIe4TMQX%2FpuYFd2FS%2BpCZRKgEQXu3pjt4hc%2F8i%2FsngswGveFa1wPOXn6AXQdGD3J2uBcaCKfgnBuPfpg0qjH0V%2Fp02r9b0lDO33v6IqDQnSifg%2F5dsKEGWTtoBhbdHGvOQb1cHSiHwveZHe0zZZ7l3kC2BD4fI5AsG%2BVBfEE9Vh7gpwT5585FouxNld1gVuAWy2QDOmHG3nphOTDIcxw5DFtIubNcy3%2BO8dsxY9QukiDGhmvQOhiOoz0plDOtmQ%2F061zgblBq1T0SZcqE%2F02BSCiyOEXb7GqPpm9xxwRCW6MjvvBoxm8zOpoL7Vdk3GothUij%2B9c682bDkeO5x%2FV2ud7ip6cNaqb%2FJXwNzJyZT66n4FLWxTvwD5s%2FteZwsYaEn0%2FBLEHQ2ERmbjmSnxSsyHkIAQlswaM0I3RvjShcBHiiw2%2F8Ame%2BsHqWGH0lwWttMsB8Ytlr7n1HOcUZI4zCgX5WnJTH9N1WkKmjl33SQzT4NnT287rY6UWvnj4gAE9RsYMMZZTvO5KR8NNuXbyicMTay6f%2BFPXpRC02jAUnzvCx1%2B%2FaslhDXejvXg9gHfOneZTFhG26C9ea1eersgzRnV6eH4VZKec3ART28FFIjq3%2F7qHmSgMMLlr8YGOpoBJX574UGoQXLLveh6hTyuAOR2BBYvFpwcBwztZPbB%2FVg3MnXq%2FOmTzrfUnBYSvCgUFmuiq8URQ5XWUuysQGGjrJ0s4xqE4USROqdaPjASL%2FNq%2Fj5nCBHARBQbVqb4YPqFAOEnVg38YNM%2F2OEgAi8b4nyQN0OoL86kfwzBqQ2sCV5VMuaM34P1heGDbTrrUWAXh%2BndqN%2FvQiWPtg%3D%3D&Expires=1758199285)