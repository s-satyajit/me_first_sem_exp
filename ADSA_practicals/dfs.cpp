#include <iostream>
#include <list>
using namespace std;

class Graph {
    int V;
    list<int>* adj;
    void DFSUtil(int v, bool visited[]) {
        visited[v] = true;
        cout << v << " ";
        for (auto i : adj[v])
            if (!visited[i])
                DFSUtil(i, visited);
    }
public:
    Graph(int V) {
        this->V = V;
        adj = new list<int>[V];
    }
    void addEdge(int v, int w) {
        adj[v].push_back(w);
    }
    void DFS(int v) {
        bool* visited = new bool[V];
        for (int i = 0; i < V; i++)
            visited[i] = false;
        DFSUtil(v, visited);
    }
};

int main() {
    Graph g(6);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 5);

    cout << "Depth First Traversal starting from vertex 0:\n";
    g.DFS(0);

    return 0;
}
