#include <iostream>
using namespace std;

// Sum
int sumArray(int a[], int num)
{
    int sum = 0;
    for (int i = 0; i < num; i++)
        sum = sum + a[i];
    return sum;
}

// Linear search
int findElement(int a[], int num, int key)
{
    for (int i = 0; i < num; i++)
    {
        if (a[i] == key) return i;
    }
    return -1;
}

// Append
int appendAtEnd(int a[], int num, int value)
{
    a[num] = value;
    return num + 1;   // new size
}

// Insert element
int insertAtIndex(int a[], int num, int index, int value)
{
    for (int i = num; i > index; i--)
    {
        a[i] = a[i - 1];
    }
    a[index] = value;
    return num + 1;
}

// Delete element
int deleteAtIndex(int a[], int num, int index)
{
    for (int i = index; i < num - 1; i++)
    {
        a[i] = a[i + 1];
    }
    return num - 1;
}

// Reverse
void reverseArray(int a[], int num)
{
    int start = 0, end = num - 1;
    while (start < end)
    {
        int temp = a[start];
        a[start] = a[end];
        a[end] = temp;
        start++;
        end--;
    }
}

// Max Element
int maxElement(int a[], int num)
{
    int max = a[0];
    for (int i = 1; i < num; i++)
    {
        if (a[i] > max) max = a[i];
    }
    return max;
}

// Minimum Element
int minElement(int a[], int num)
{
    int min = a[0];
    for (int i = 1; i < num; i++)
    {
        if (a[i] < min) min = a[i];
    }
    return min;
}

// Average
float averageArray(int a[], int num)
{
    int sum = sumArray(a, num);
    return (float)sum / num;
}


void printArray(int a[], int num)
{
    for (int i = 0; i < num; i++)
        cout << a[i] << " ";
    cout << endl;
}

int main()
{
    int a[20] = {10, 25, 3, 47, 8, 16};
    int num = 6;

    cout << "Original array: ";
    printArray(a, num);

    cout << "Sum: " << sumArray(a, num) << endl;
    cout << "Average: " << averageArray(a, num) << endl;
    cout << "Max: " << maxElement(a, num) << endl;
    cout << "Min: " << minElement(a, num) << endl;

    int key = 47;
    int idx = findElement(a, num, key);
    if (idx != -1)
        cout << "Found " << key << " at index " << idx << endl;
    else
        cout << key << " not found" << endl;

    num = appendAtEnd(a, num, 99);
    cout << "After append 99: ";
    printArray(a, num);

    num = insertAtIndex(a, num, 2, 55);
    cout << "After inserting 55 at index 2: ";
    printArray(a, num);

    num = deleteAtIndex(a, num, 0);
    cout << "After deleting index 0: ";
    printArray(a, num);

    reverseArray(a, num);
    cout << "After reversing: ";
    printArray(a, num);

    return 0;
}
