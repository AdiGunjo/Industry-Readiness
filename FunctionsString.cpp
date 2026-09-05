#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
using namespace std;

// 1. String Length
int stringLength(string s) {
    return s.length();
}

// 2. Reverse a String
string reverseString(string s) {
    reverse(s.begin(), s.end());
    return s;
}

// 3. Convert to Uppercase
string toUpperCase(string s) {
    for (int i = 0; i < s.length(); i++)
        s[i] = toupper(s[i]);
    return s;
}

// 4. Convert to Lowercase
string toLowerCase(string s) {
    for (int i = 0; i < s.length(); i++)
        s[i] = tolower(s[i]);
    return s;
}

// 5. Check Palindrome
bool isPalindrome(string s) {
    string rev = s;
    reverse(rev.begin(), rev.end());
    return s == rev;
}

// 6. Count Vowels
int countVowels(string s) {
    int count = 0;
    string vowels = "aeiouAEIOU";
    for (char c : s)
        if (vowels.find(c) != string::npos)
            count++;
    return count;
}

// 7. Concatenate Two Strings
string concatenateStrings(string s1, string s2) {
    return s1 + s2;
}

// 8. Find and Replace First Occurrence
string findAndReplace(string s, string toFind, string replaceWith) {
    size_t pos = s.find(toFind);
    if (pos != string::npos)
        s.replace(pos, toFind.length(), replaceWith);
    return s;
}

// 9. Split String by Delimiter
vector<string> splitString(string s, char delimiter) {
    vector<string> tokens;
    stringstream ss(s);
    string token;
    while (getline(ss, token, delimiter))
        tokens.push_back(token);
    return tokens;
}

// 10. Remove Whitespaces
string removeSpaces(string s) {
    s.erase(remove(s.begin(), s.end(), ' '), s.end());
    return s;
}

int main() {
    string sample = "Hello World";

    cout << "\n1. String Length" << endl;
    cout << stringLength(sample) << endl;

    cout << "\n2. Reverse a String" << endl;
    cout << reverseString(sample) << endl;

    cout << "\n3. Convert to Uppercase" << endl;
    cout << toUpperCase(sample) << endl;

    cout << "\n4. Convert to Lowercase" << endl;
    cout << toLowerCase(sample) << endl;

    cout << "\n5. Check Palindrome" << endl;
    string palTest = "madam";
    cout << palTest << " -> " << (isPalindrome(palTest) ? "Palindrome" : "Not a palindrome") << endl;

    cout << "\n6. Count Vowels" << endl;
    cout << "Vowels in \"" << sample << "\": " << countVowels(sample) << endl;

    cout << "\n7. Concatenate Two Strings" << endl;
    cout << concatenateStrings("Coffee", "Script") << endl;

    cout << "\n8. Find and Replace First Occurrence" << endl;
    cout << findAndReplace(sample, "World", "C++") << endl;

    cout << "\n9. Split String by Delimiter" << endl;
    vector<string> parts = splitString("apple,banana,cherry", ',');
    for (const string &part : parts)
        cout << part << endl;

    cout << "\n10. Remove Whitespaces" << endl;
    cout << removeSpaces("  H e l l o  ") << endl;

    return 0;
}