#include <bits/stdc++.h>
using namespace std;

pair<long long, long long> selectionSort(vector<int>& arr) {
    long long comparisons = 0;
    long long swaps = 0;
    int n = (int)arr.size();

    for (int i = 0; i < n - 1; ++i) {
        int minIdx = i;
        for (int j = i + 1; j < n; ++j) {
            ++comparisons;
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        if (minIdx != i) {
            swap(arr[i], arr[minIdx]);
            ++swaps;
        }
    }
    return {comparisons, swaps};
}

void printVector(const vector<int>& v) {
    cout << "[";
    for (size_t i = 0; i < v.size(); ++i) {
        cout << v[i] << (i + 1 < v.size() ? ", " : "");
    }
    cout << "]";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<vector<int>> tests = {
        {64, 25, 12, 22, 11},
        {5, 4, 3, 2, 1},
        {1, 2, 3, 4, 5},
        {3, 3, 2, 1, 3}
    };

    for (size_t t = 0; t < tests.size(); ++t) {
        vector<int> a = tests[t];
        cout << "\nTest #" << (t + 1) << ":\n";
        cout << "Input:  ";
        printVector(a);
        cout << "\n";

        auto [comparisons, swaps] = selectionSort(a);

        cout << "Sorted: ";
        printVector(a);
        cout << "\nComparisons: " << comparisons << ", Swaps: " << swaps << "\n";
    }

    return 0;
}
