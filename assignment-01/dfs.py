# Define constants
N = 1000002

# Function to input the graph
def graph_input():
    n, m = map(int, input().split())
    print("Enter the edges (format: u v):")
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    return n, g

# Function to print the graph
def print_graph(n, g):
    for i in range(1, n+1):
        print(i, "->", end=" ")
        for d in g[i]:
            print(d, end=" ")
        print()

# Helper function for DFS
def dfs_visit(node, visited, g):
    visited[node] = True
    print(node, end=" ")

    for neighbor in g[node]:
        if not visited[neighbor]:
            dfs_visit(neighbor, visited, g)

# DFS function
def dfs(start, n, g):
    visited = [False] * (n+1)
    print("DFS Traversal:", end=" ")
    dfs_visit(start, visited, g)
    print()

# Main function
def main():
    n, g = graph_input()
    print_graph(n, g)
    
    start_node = int(input("Enter the starting node for DFS and BFS: "))
    
    dfs(start_node, n, g)
    

if __name__ == "__main__":
    main()
