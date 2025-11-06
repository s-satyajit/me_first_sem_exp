#include <bits/stdc++.h>
using namespace std;

void bubbleSort(int arr[], int size) {
    for(int i = 0; i < size-1; i++) {
        for(int j = 0; j < size-i-1; j++) {
            if(arr[j] > arr[j+1]){
                // swap(arr[j], arr[j+1])
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

void printArray(int arr[], int size) {
    for(int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
}

int main() {
    int data[] = {1, 4, 0, 2, 8, 3};

    int size = sizeof(data) / sizeof(data[0]);
    
    bubbleSort(data, size);
    cout << data << " --> gives pointer value \n";  //gives pointer value
    printArray(data, size); //gives the actual value inside the array

    return 0;
}