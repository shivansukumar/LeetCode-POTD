class Solution:
    def __init__(self):
        self.result = 0
        self.digit = [0] * 10

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.result

    def dfs(self, root: TreeNode) -> None:
        if not root:
            return

        self.digit[root.val] += 1

        if not root.left and not root.right:
            if self.is_palindrome():
                self.result += 1
        else:
            self.dfs(root.left)
            self.dfs(root.right)

        self.digit[root.val] -= 1

    def is_palindrome(self) -> bool:
        odd = sum(1 for freq in self.digit[1:10] if freq % 2 != 0)
        return odd <= 1