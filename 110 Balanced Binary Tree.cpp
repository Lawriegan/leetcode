#include <iostream>
#include <cstdio>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (!root) return true;
        bool balanced = true;
        height(root, &balanced);
        return balanced;
    }

    int height(TreeNode* node, bool* balanced){
        if (!balanced) return -1;
        if (!node) return 0;
        int left_height = height(node->left, balanced);
        int right_height = height(node->right, balanced);
        if (abs(left_height-right_height) > 1){
            *balanced = false;
            return -1;
        }
        return max(left_height, right_height) + 1;
    }
};