#include <cstdio>
#include <iostream>

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    int rob(TreeNode* root) {
        if (root == NULL) {
        	return 0;
        } 
        else {
        	int ChooseRoot = root->val;
        	if (root->left) {
        		ChooseRoot += (rob(root->left->left) + rob(root->left->right));
        	}
        	if (root->right) {
        		ChooseRoot += (rob(root->right->left) + rob(root->right->right));
        	}
        	int NotChooseRoot = 0;
        	NotChooseRoot += (rob(root->left) + rob(root->right));
        	if (ChooseRoot > NotChooseRoot)
        		result = ChooseRoot;
        	else
        		result = NotChooseRoot;
        	return result;
        }
    }
};