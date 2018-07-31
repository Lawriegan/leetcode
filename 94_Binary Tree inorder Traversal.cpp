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
        stack<TreeNode*> helper; // traversal with stack 

        TreeNode *currentNode;
        helper.push(root);
        bool leftVisited = false; 
        // mark that left child of current node is visited
        
        while (!helper.empty()) {
            currentNode = helper.top();

            // if left child is not empty and has not been visited
            if (currentNode->left && !leftVisited){
                helper.push(currentNode->left);
            }
            else{
                result.push_back(currentNode->val);
                helper.pop();
                leftVisited = true;
                if (currentNode->right){
                    helper.push(currentNode->right);
                    leftVisited = false;
                }
            }
        }
        return result;
    }
    vector<int> inorderTraversal2(TreeNode* root) {
        vector<int> result;
        if (!root)
            return result;
        stack<TreeNode*> helper; // traversal with stack 

        TreeNode *currentNode = root;
    
        while (currentNode || !helper.empty()) {
            while (currentNode){
                helper.push(currentNode);
                currentNode = currentNode->left;
            }
            // if left child is not empty and has not been visited

            if (!helper.empty()){
                currentNode = helper.top();
                result.push_back(currentNode->val);
                helper.pop();
                currentNode = currentNode->right;
            }
        }
        return result;
    }
};