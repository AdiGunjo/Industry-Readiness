#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Helper to print a vector
void printVector(vector<int> arr) {
    for (int x : arr)
        cout << x << " ";
    cout << endl;
}

// 1. Find Maximum Element
int findMax(vector<int> arr) {
    return *max_element(arr.begin(), arr.end());
}

// 2. Find Minimum Element
int findMin(vector<int> arr) {
    return *min_element(arr.begin(), arr.end());
}

// 3. Reverse an Array
vector<int> reverseArray(vector<int> arr) {
    reverse(arr.begin(), arr.end());
    return arr;
}

// 4. Sort an Array
vector<int> sortArray(vector<int> arr) {
    sort(arr.begin(), arr.end());
    return arr;
}

// 5. Search for an Element (Linear Search)
int linearSearch(vector<int> arr, int target) {
    for (int i = 0; i < arr.size(); i++)
        if (arr[i] == target)
            return i;
    return -1;
}

// 6. Remove Duplicates
vector<int> removeDuplicates(vector<int> arr) {
    sort(arr.begin(), arr.end());
    arr.erase(unique(arr.begin(), arr.end()), arr.end());
    return arr;
}

// 7. Merge Two Arrays
vector<int> mergeArrays(vector<int> a, vector<int> b) {
    vector<int> result = a;
    result.insert(result.end(), b.begin(), b.end());
    return result;
}

// 8. Rotate Array Left by k Positions
vector<int> rotateLeft(vector<int> arr, int k) {
    k = k % arr.size();
    rotate(arr.begin(), arr.begin() + k, arr.end());
    return arr;
}

// 9. Check if Array is Sorted
bool isSorted(vector<int> arr) {
    return is_sorted(arr.begin(), arr.end());
}

// 10. Count Occurrences of an Element
int countOccurrences(vector<int> arr, int target) {
    return count(arr.begin(), arr.end(), target);
}

int main() {
    vector<int> sample = {5, 3, 8, 1, 9, 3, 5, 2};

    cout << "Sample array: ";
    printVector(sample);

    cout << "\n1. Find Maximum Element" << endl;
    cout << findMax(sample) << endl;

    cout << "\n2. Find Minimum Element" << endl;
    cout << findMin(sample) << endl;

    cout << "\n3. Reverse an Array" << endl;
    printVector(reverseArray(sample));

    cout << "\n4. Sort an Array" << endl;
    printVector(sortArray(sample));

    cout << "\n5. Search for an Element (Linear Search)" << endl;
    int target = 8;
    int idx = linearSearch(sample, target);
    cout << "Index of " << target << ": " << idx << endl;

    cout << "\n6. Remove Duplicates" << endl;
    printVector(removeDuplicates(sample));

    cout << "\n7. Merge Two Arrays" << endl;
    vector<int> a = {1, 2, 3};
    vector<int> b = {4, 5, 6};
    printVector(mergeArrays(a, b));

    cout << "\n8. Rotate Array Left by k Positions" << endl;
    printVector(rotateLeft(sample, 3));

    cout << "\n9. Check if Array is Sorted" << endl;
    vector<int> sortedArr = {1, 2, 3, 4, 5};
    cout << (isSorted(sortedArr) ? "Sorted" : "Not sorted") << endl;
    cout << (isSorted(sample) ? "Sorted" : "Not sorted") << endl;

    cout << "\n10. Count Occurrences of an Element" << endl;
    int val = 3;
    cout << "Occurrences of " << val << ": " << countOccurrences(sample, val) << endl;

    return 0;
}