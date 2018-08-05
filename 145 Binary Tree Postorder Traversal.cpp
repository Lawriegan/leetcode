#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <deque>
using namespace std;
 
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
class Solution {
public:
    // vector<int> postorderTraversal(TreeNode* root) {
    //     vector<int> result;
    //     if (!root) 
    //         return result;
    //     stack<TreeNode*> helper;
    //     stack<int> ans;
    //     helper.push(root);
    //     while(!helper.empty()){
    //         TreeNode* curNode = helper.top();
    //         helper.pop();
    //         ans.push(curNode->val);
    //         if (curNode->left) helper.push(curNode->left);
    //         if (curNode->right) helper.push(curNode->right);
    //     }
    //     while (!ans.empty()) {
    //         result.push_back(ans.top());
    //         ans.pop();
    //     }
    //     return result;
    // }
    vector<int> postorderTraversal2(TreeNode* root) {
        deque<int> result;
        // if (!root) 
        //     return {};  // c++11
        stack<TreeNode*> helper;
        helper.push(root);
        while(!helper.empty()){
            TreeNode* curNode = helper.top();
            helper.pop();
            result.push_front(curNode->val);
            if (curNode->left) helper.push(curNode->left);
            if (curNode->right) helper.push(curNode->right);
        }
        return vector<int> (result.begin(), result.end());
    }
};