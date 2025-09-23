#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout << "Enter number of names: ";
    if (!(cin >> n)) return 0;

    vector<string> a(n);
    for (int i = 0; i < n; ++i) {
        cout << "Enter name " << i + 1 << ": ";
        cin >> ws;
        getline(cin, a[i]);
    }

    cout << "enter an element: ";
    string key;
    getline(cin, key);

    int pos = -1;
    for (int i = 0; i < n; ++i) {
        if (a[i] == key) {
            pos = i + 1;
            break;
        }
    }

    if (pos == -1) cout << "Search result: Name not found\n";
    else cout << "Search result: Name found at position " << pos << "\n";

    return 0;
}
