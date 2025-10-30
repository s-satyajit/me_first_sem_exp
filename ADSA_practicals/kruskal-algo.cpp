#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Edge {
public:
    int src, dest, weight;
};

int findParent(int v, vector<int>& parent) {
    if (v == parent[v]) return v;
    return findParent(parent[v], parent);
}

void unionSets(int a, int b, vector<int>& parent, vector<int>& rank) {
    a = findParent(a, parent);
    b = findParent(b, parent);
    if (a != b) {
        if (rank[a] < rank[b]) swap(a, b);
        parent[b] = a;
        if (rank[a] == rank[b]) rank[a]++;
    }
}

bool compare(Edge a, Edge b) {
    return a.weight < b.weight;
}

int main() {
    int V = 5, E = 7;
    vector<Edge> edges = {
        {0, 1, 9},
        {0, 2, 75},
        {1, 2, 95},
        {1, 3, 19},
        {1, 4, 42},
        {2, 3, 51},
        {3, 4, 31}
    };

    sort(edges.begin(), edges.end(), compare);

    vector<int> parent(V);
    vector<int> rank(V, 0);
    for (int i = 0; i < V; i++) parent[i] = i;

    vector<Edge> result;
    int totalWeight = 0;

    for (auto e : edges) {
        int uParent = findParent(e.src, parent);
        int vParent = findParent(e.dest, parent);
        if (uParent != vParent) {
            result.push_back(e);
            totalWeight += e.weight;
            unionSets(uParent, vParent, parent, rank);
        }
    }

    cout << "Edge : Weight\n";
    for (auto e : result)
        cout << e.src << " - " << e.dest << " : " << e.weight << endl;

    cout << "Total Weight of MST: " << totalWeight << endl;
    return 0;
}
