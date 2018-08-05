#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> helper;
        int length = nums.size();
        int result = nums[0];

        if (length == 0){
            return 0;
        }
        helper.push_back(nums[0]);
        bool all_minus = true;
        for (int i = 1; i < length; ++i) {
            if (helper[i-1] > 0) {
                helper.push_back(helper[i-1] + nums[i]);
                all_minus = false;
            }
            else {
                helper.push_back(nums[i]);
            }
        }
        if (all_minus){
            for (vector<int>::iterator it = nums.begin(); it != nums.end(); it++){
                result = max(result, *it);
            }
            return result;
        }
        
        for (vector<int>::iterator it = helper.begin(); it != helper.end(); it++){
            result = max(result, *it);
        }
        return result;
    }
};

Solution s;
//s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]);