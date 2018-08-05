#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    string tree2str(TreeNode* t) {
        if (t == nullptr) return "";
        const string s = to_string(t->val);
        const string l = tree2str(t->left);
        const string r = tree2str(t->right);
        // case 0 s
        if (t->left == nullptr && t->right == nullptr) return s;
        // case 1 s(l)
        if (t->right == nullptr) return s + '(' + l + ')';
        // general case s(l)(r)
        return s + '(' + l + ')' + '(' + r + ')';
    }
};