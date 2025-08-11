#include"bits/stdc++.h"
using namespace std;

vector<int> shelf;
vector<int> book;
int n,m,x,y;

bool check(int arts){
    vector<int> places(n,x);
    for (int i = n - arts;i < n;i++) places[i] = y;
    int bi = 0;
    int si = 0;
    while (bi < m && si < n){
        if (places[si] > 0 && book[bi] <= shelf[si]){
            places[si]--;
            bi++;
        } else if (places[si] == 0){
            si++;
        } else if (book[bi] > shelf[si]){
            return false;
        }
    }
    
    return bi == m;
}


int main() {
    cin >> n >> m >> x >> y;
    shelf.resize(n);book.resize(m);

    for (int i=0;i<n;i++)cin >> shelf[i];
    for (int i=0;i<m;i++)cin >> book[i];

    sort(shelf.begin(),shelf.end(),greater<>());
    sort(book.begin(),book.end(),greater<>());
    
    int low,high,mid;
    low = 0;high = n;mid = (low + high) / 2;
    
    while (high - low > 1){
        mid = (low + high) / 2;
        if (check(mid)){
            low=mid;
        } else {
            high=mid;
        }
    }

    for (auto e:{high,mid,low}){
        if (check(e)){
            cout << e << "\n";
            return 0;
        }
    }
    cout << "impossible" << "\n";
}