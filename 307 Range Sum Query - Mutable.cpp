#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

class NumArray {
public:
    NumArray(vector<int> nums) {
        nums_ = nums;
        size = nums.size();
        for (int i = 0; i < size+1; ++i){
            sums_.push_back(0);
        }
        sums_[0] = 0;
        for (int i = 1; i < size+1; ++i){
            updateSum_(i, nums_[i-1]);
        }
    }
    void update(int i, int val) {
        int origin_num = nums_[i];
        nums_[i] = val;
        updateSum_(i+1, val-origin_num);
    }

    
    int sumRange(int i, int j) {
        int sum1 = query(i);
        int sum2 = query(j+1);
        return sum2-sum1;
    }
private:
    vector<int> nums_;
    vector<int> sums_;
    static inline int lowbit(int x) {
        return x & (-x);
    }
    int size;
    void updateSum_(int i, int delta) {
        while (i < sums_.size()) {
            sums_[i] += delta;
            i += lowbit(i);
        }
    }
    int query(int i) const {
        int sum = 0;
        while(i > 0) {
            sum += sums_[i]; 
            i -= lowbit(i);
        }
        return sum;
    }
};
