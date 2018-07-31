//
//  8_String to Integer (atoi).h
//  leetcode
//
//  Created by 李根 on 2018/3/3.
//  Copyright © 2018年 李根. All rights reserved.
//

#ifndef __String_to_Integer__atoi__h
#define __String_to_Integer__atoi__h

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
class atoi {
public:
    int myAtoi(string str) {
        bool flag = false;
        int num = 0;
        int sign = 1;
        for (int i = 0; str[i]!='\0';++i){
            if (str[i]!=' '){
                if (!flag){
                    if (str[i] == '-'){
                        sign = -1;
                        flag = true;
                    }
                    else if (str[i] == '+'){
                        flag = true;
                    }
                    else if (str[i] >= '0' && str[i] <= '9'){
                        num += num*10 + str[i] - '0';
                        flag = true;
                    }
                    else
                        break;
                }
                else{
                    if (str[i] >= '0' && str[i] <= '9'){
                        num += num*10 + str[i] - '0';
                    }
                    else break;
                }
            }
        }
        return num*sign;
    }
};

#endif /* __String_to_Integer__atoi__h */
