# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        val = root.val
        left_list = self.preorderTraversal(root.left)
        right_list = self.preorderTraversal(root.right)
        return [val] + left_list + right_list

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        left_list = self.inorderTraversal(root.left)
        val = root.val
        right_list = self.inorderTraversal(root.right)
        return left_list + [val] + right_list

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        left_list = self.postorderTraversal(root.left)
        right_lift = self.postorderTraversal(root.right)
        val = root.val
        return left_list + right_lift + [val]

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ans = []
        bfs_q = []
        bfs_q.append(root)

        while bfs_q:
            level_items = []
            len_q = len(bfs_q)
            for i in range(len_q):
                pop_node = bfs_q.pop(0)
                level_items.append(pop_node.val)
                if pop_node.left:
                    bfs_q.append(pop_node.left)
                if pop_node.right:
                    bfs_q.append(pop_node.right)
            ans.append(level_items)
        return ans

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def checkSymmetry(left_sub_tree, right_sub_tree):
            if left_sub_tree == None and right_sub_tree == None:
                return True
            elif right_sub_tree is not None and left_sub_tree is not None:
                if (left_sub_tree.val == right_sub_tree.val) and checkSymmetry(left_sub_tree.left,
                                                                               right_sub_tree.right) and checkSymmetry(
                    left_sub_tree.right, right_sub_tree.left):
                    return True
            return False

        if root is None:
            return True
        return checkSymmetry(root.left, root.right)

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return (sum == 0)
        else:
            subtracted_sum = sum - root.val

            if subtracted_sum == 0 and root.left == None and root.right == None:
                return True
            if root.left is not None:
                self.hasPathSum(root.left, subtracted_sum)
            if root.right is not None:
                self.hasPathSum(root.right, subtracted_sum)
            return False

    def hasPathSumWithPath(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return None

        stack = []
        stack.append((root, 0, []))

        while stack:

            node, cur_sum, path = stack.pop()
            path.append(node)
            cur_sum += node.val

            if not node.left and not node.right:
                if cur_sum == sum:
                    return True
            if node.left:
                stack.append((node.left, cur_sum, path[:]))
            if node.right:
                stack.append((node.right, cur_sum, path[:]))
        return False