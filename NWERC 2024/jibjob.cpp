#include"bits/stdc++.h"
using namespace std;

int dist(int x,int y,int xx,int yy){
    return (int) sqrt(pow(x - xx,2) + pow(y - yy,2));
}

int main() {
    int n;cin >> n;
    vector<vector<double>> cranes(n);
    for (int i = 0;i < n;i++){
        double a,b,c;cin>>a>>b>>c;
        cranes[i]={a,b,c};
    }
    for (int i = 0;i < n;i++){
        int mn = cranes[i][2];
        for (int j = 0;j < n;j++){
            if (j == i || cranes[i][2] > cranes[j][2])continue;
            mn = min(mn,dist(cranes[i][0],cranes[i][1],cranes[j][0],cranes[j][1]));
        }
        cout << mn << "\n";
    }
}