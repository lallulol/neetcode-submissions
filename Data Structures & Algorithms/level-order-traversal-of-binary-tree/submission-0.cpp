/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
   public:
    vector<vector<int>> answer;
    void order(TreeNode* root, int level) {
        if (root == nullptr) {
            return;
        }
        if (answer.size() == level) {
            answer.push_back({});
        }
        answer[level].push_back(root->val);
        order(root->left, level + 1);
        order(root->right, level + 1);
    }

    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        answer.clear();
        order(root, 0);
        return answer;
    }
};
