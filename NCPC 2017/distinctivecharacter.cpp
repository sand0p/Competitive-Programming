#include<bits/stdc++.h>
using namespace std;
#define pii pair<int,int>

int main(){
    int q,l;
    cin>>q>>l;
    vector<int> start_nodes;
    for (int i=0;i<q;i++){
        int num=0;
        for (int j=0;j<l;j++){
            char c;cin>>c;
            num=(num<<1) | (c - '0');
        }
        start_nodes.push_back(num);
    }

    vector<bool> visited(pow(2,l)+1,false);
    queue<int> Q;
    for (int e:start_nodes)Q.push(e);

    int last=0;
    while (!Q.empty()){
        int node=Q.front();Q.pop();
        if (visited[node])continue;
        visited[node]=true;
        last=node;
        for (int i=0;i<l;i++){
            int next=node^(1<<i);
            if (visited[next])continue;
            Q.push(next);
        }

    }
    cerr << last << endl;
    string res;
    while (last>0){
        res = (last % 2 == 0 ? "0" : "1") + res;
        last /= 2;
    }
    while (res.size()<l)res="0"+res;
    cout << res << "\n";


}