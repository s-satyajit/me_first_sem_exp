#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define INF 9999999

void dijkstra(int V, vector<vector<pair<int, int>>> adj, int src) {
    vector<int> dist(V, INF);
    dist[src] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        for (auto edge : adj[u]) {
            int v = edge.first;
            int weight = edge.second;
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    cout << "Vertex\tDistance from Source\n";
    for (int i = 0; i < V; i++)
        cout << i << "\t" << dist[i] << endl;
}

int main() {
    int V = 6;
    vector<vector<pair<int, int>>> adj(V);

    adj[0].push_back({1, 4});
    adj[0].push_back({2, 2});
    adj[1].push_back({2, 5});
    adj[1].push_back({3, 10});
    adj[2].push_back({4, 3});
    adj[4].push_back({3, 4});
    adj[3].push_back({5, 11});
    adj[4].push_back({5, 5});

    dijkstra(V, adj, 0);
    return 0;
}
