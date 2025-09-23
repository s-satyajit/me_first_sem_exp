#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout << "Enter number of elements: ";
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    cout << "Enter elements:\n";
    for (int i = 0; i < n; ++i) {
        cout << "Element " << i << ": ";
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    cout << "Sorted array: ";
    for (int i = 0; i < n; ++i) {
        cout << a[i] << " ";
    }
    cout << "\n";

    cout << "enter an element: ";
    int key;
    cin >> key;

    int low = 0, high = n - 1;
    int pos = -1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == key) {
            pos = mid;
            break;
        } else if (a[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    if (pos == -1) cout << "Search result: Element not found\n";
    else cout << "Search result: Element found at index " << pos << "\n";

    return 0;
}