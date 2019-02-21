---
layout: page
title: Binary Trees
permalink: /notes/data-structures/binary-trees
---

Binary trees are recursively defined: it can be empty, or a root with left and right trees, which are also binary trees (empty or a root to another tree) and so on... 

One important use of binary trees are a binary search tree, however, there are many other applications of binary trees.

* The depth of a node *n* is the number of nodes in the search path from the root, not including the node itself.
* The height of a tree is given by the node w/ the maximum depth.
* A full binary tree has all nodes with either 0 or 2 subtrees.
* A perfect binary tree is a full tree it’s full w/ all leaves of the same depth, and every parent has two children.
* A complete tree is filled except the last depth, which is filled from left to right.
* We can do three different kinds of traversals for trees:
  * Preorder: we visit the node, then it's left and right subtrees
  * Inorder: we visit the left subtree, then the node, then the right subtree
  * Postorder: we visit the left subtree, the right subtree, then the node
* It's important to note that the preorder traversal and postorder traversals, if we include null leaves, are unique for a tree, whereas the inorder traversal w/ null leaves is not.
* Recursive algorithms tend to work well with tree problems.
* When thinking about worst case complexity, consider right- and left-skewed trees (a big ol stick)


### Problems

#### Test if a binary tree is height balanced

* For a binary tree, height balanced means that for every node, the depths of both subtrees do not differ by more than 1.
* Lets write a function that takes in a binary tree root node, and returns if the tree is balanced or not.

```
private static class BalanceStatusWithHeight {
  public boolean balanced;
  public int height;
  public BalanceStatusWithHeight(boolean balanced, int height) {
    this.balanced = balanced;
    this.height = height;
  }
}

private static BalanceStatusWithHeight checkBalanced(BinaryTreeNode<Integer> tree) {
  if (tree == null) {
    return new BalanceStatusWithHeight(true, -1);
  }
  BalanceStatusWithHeight leftBalance = checkBalanced(tree.left);
  if (!leftBalance.balanced) {
    return leftBalance;
  }
  BalanceStatusWithHeight rightBalance = checkBalanced(tree.right);
  if (!rightBalance.balanced) {
    return rightBalance;
  }
  boolean isBalanced = Math.abs(leftBalance.height, - rightBalance.height) <= 1;
  int maxHeight = Math.max(leftBalance.height, rightBalance.height) + 1;
  return new BalanceStatusWithHeight(isBalanced, maxHeight);
}

public static boolean isBalanced(BinaryTreeNode<Integer> tree) {
  return checkBalanced(tree).balanced;
}

```
