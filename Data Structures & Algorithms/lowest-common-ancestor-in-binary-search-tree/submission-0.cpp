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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr || root == p || root == q) return root;

        TreeNode* left_side = lowestCommonAncestor(root->left, p, q);
        TreeNode* right_side = lowestCommonAncestor(root->right, p, q);

        if (left_side != nullptr && right_side != nullptr) {
            return root;   
        }
        if(left_side != nullptr) {
            return left_side;
        }
        if (right_side != nullptr) {
            return right_side;
        }
        return nullptr;
    }
};
