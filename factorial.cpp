#include <bits/stdc++.h>

using namespace std;

int main()
{
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   cout.tie(NULL);
#ifndef ONLINE_JUDGE
   freopen("input.txt", "r", stdin);
#endif

   int n;
   cin >> n;
   for (int i = 0; i < n; i++)
   {
      cout << (i + 1) << ' ';
   }
   cout << '\n';
   return 0;
}