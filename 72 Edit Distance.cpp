#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int len1 = word1.size();
        int len2 = word2.size();
        if (len1 == 0 || len2 == 0){
            return len1+len2;
        }
        int **dist = new int *[len1+1];
        for (int i = 0; i <= len1; ++i){
            dist[i] = new int[len2+1];
            dist[i][0] = i;
        }
        
        for (int j = 0; j <= len2; ++j){
            dist[0][j] = j;
        }
        int flag = 0;
        for (int i = 1; i <= len1; ++i) {
            for (int j = 1; j <= len2; ++j) {
                if (word1[i-1] == word2[j-1]) {
                    flag = 0;
                }
                else{
                    flag = 1;
                }
                dist[i][j] = min(min(dist[i-1][j]+1, dist[i][j-1]+1), dist[i-1][j-1]+flag);
            }
        }
        return dist[len1][len2];
    }
};