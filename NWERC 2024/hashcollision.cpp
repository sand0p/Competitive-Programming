#include"bits/stdc++.h"
using namespace std;

int ask(int c,int r) {
    cout << "? " << c << " " << r << "\n";
    int res;cin >> res;
    return res;
}

int main() {
    int n;cin >> n;
    int x = 1;
    int r1 = ask(n,x);
    if (n == r1){
        cout <<"! "<< r1 << " " << x << "\n";
    } else {
        int r2 = ask(n-r1,x);
        cout << "! " << r1 << " " << r2 << "\n";
    }
}