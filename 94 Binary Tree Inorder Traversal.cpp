#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>

using namespace std;


struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        if (!root)
            return result;
        stack<int> helper;
        
        TreeNode *currentNode = root;
        helper.push(currentNode->val);

        while (currentNode) {

        }

    }
};