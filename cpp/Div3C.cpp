#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n, k, x;
        cin >> n >> k >> x;
        
        if (k * (k - 1) / 2 >= x) {
            cout << "NO" << endl;
            continue;
        }
        
        if (k * (2 * n - k + 1) / 2 <= x) {
            cout << "NO" << endl;
            continue;
        }
        
        cout << "YES" << endl;
    }
    
    return 0;
}
