#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <initializer_list>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    // vector<vector<int> > levelOrder(TreeNode* root) {
    //     vector<vector<int> > result;
    //     queue<TreeNode*> q;
    //     q.push(root);
    //     int last = q.size();
    //     int cur = 0;
    //     vector<int> *temp = new vector<int>;
    //     if (root == nullptr) {
    //         return result;
    //     }
    //     while(!q.empty()){    
    //         TreeNode *curNode = q.front();
    //         q.pop();
    //         (*temp).push_back(curNode->val);
    //         cur++;
    //         if (curNode->left){
    //             q.push(curNode->left);
    //         }
    //         if (curNode->right){
    //             q.push(curNode->right);
    //         }
    //         if (cur == last){   // 当前层遍历完
    //             result.push_back(*temp);
    //             last = q.size();
    //             (*temp).clear();
    //             //vector<int> *temp = new vector<int>;
    //             cur = 0;
    //             //cout << (*temp).size() << endl;
    //         }
    //     }
    //     delete temp;
    //     return result;
    // }
    vector< vector<int> > BFS(TreeNode* root) {
        vector<int> result;
        // if (!root) return {};
        vector<vector<int> > ans;
        vector<TreeNode*> cur, next;
        cur.push_back(root);
        while (!cur.empty()){
            // ans.push_back({});
            for (TreeNode* node: cur){
                ans.back().push_back(node->val);
                if (node->left) next.push_back(node->left);
                if (node->right) next.push_back(node->right);
            }
            cur.swap(next);
            next.clear();
        }
        return ans;
    }

    void DFS(TreeNode* root, int depth, vector<vector<int> >& ans){
        if (!root) return;

        // while(ans.size() <= depth)  ans.push_back({});
        DFS(root->left, depth+1, ans);
        DFS(root->right, depth+1, ans);
        ans[depth].push_back(root->val);
    }
};