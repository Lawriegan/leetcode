//
//  6.cpp
//  leetcode
//
//  Created by 李根 on 2018/3/1.
//  Copyright © 2018年 李根. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        int len = s.length();
        if (numRows == 1){
            return s;
        }
        int remainChar = len % (2*numRows-2);
        int Cycle = len / (2*numRows-2);
        int numColumn = len / (2*numRows-2) * (numRows-1) + (max(remainChar - numRows, 0) + 1);
        //cout << numColumn << endl;
        char c[numRows+1][numColumn+1];
        for (int i = 0; i < numRows+1; i++){
            for (int j = 0; j < numColumn+1; j++){
                c[i][j] = '\0';
            }
        }
        int cycle = 0,row = 0, col = 0;
        for (int i = 0; i < len; ++i){
            if (i % (2*numRows-2) < (numRows-1) ){
                c[row][col] = s[i];
                row++;
            }
            else{
                c[row][col] = s[i];
                row--;col++;
            }
        }
        string res;
        for (int i = 0; i <= numRows; ++i){
            for (int j = 0; j <= numColumn; ++j){
                if (c[i][j] != '\0')
                    res+=c[i][j];
            }
        }
        res+='\0';
        return res;
    }
    //another answer
    /*
     string convert(string s, int nRows) {
     
     if (nRows <= 1)
     return s;
     
     const int len = (int)s.length();
     string *str = new string[nRows];
     
     int row = 0, step = 1;
     for (int i = 0; i < len; ++i)
     {
     str[row].push_back(s[i]);
     
     if (row == 0)
     step = 1;
     else if (row == nRows - 1)
     step = -1;
     
     row += step;
     }
     
     s.clear();
     for (int j = 0; j < nRows; ++j)
     {
     s.append(str[j]);
     }
     
     delete[] str;
     return s;
     }
     */
};
