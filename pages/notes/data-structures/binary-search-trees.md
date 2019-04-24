---
layout: page
title: Binary Search Trees
permalink: /notes/data-structures/binary-search-trees
---

Binary search trees are a tree such that 
  
  **a.** Each node only has two children, a right and left subtree, and 
  
  **b.** The key for each node is >= all the keys stored in it's left subtree and <= the keys stored in the nodes of its right subtree. 

BSTs are similar to sorted arrays in that the stored values are also ordered, however, the insert and deletion methods are much more efficient for a BST over an array.

Key lookup, insertion, and deletion take time proportional to the height of the tree, which in worst case can be O(n), if insertions and deletions are naively implemented. Ideally, we guarantee that the tree has height log n, which may require storing additional data at each node. Red-black trees are an example of height-balanced binary search trees and are widely used in data structure libraries.

Note: an inorder traversal yielding in order nodes means that the binary tree does satisfy the BST property as well.

We always want to avoid putting mutable objects in a BST, as a lookup for an updated object may not return the right thing or anything at all.

A BST prototype:
```
public class BstNode<T> extends TreeLike<T, BstNode<T>> {
  public T data;
  public BstNode<T> left, right;
}
```

**Searching** is the single most fundamental operation of BSTs. We can find min/max elements, and next largest/smallest, unlike a hash table. However, they also take O(log n) rather than O(1), and they do take up more space.

The following is a function which checks if a value is in a BST. (Time complexity is O(h), where h is the height of the tree.)
```
public static BstNode<Integer> searchBST(BstNode<Integer> tree, int key) {
  return tree == null || tree.data == key ? 
    tree 
    : (key < tree.data) ? searchBST(tree.left, key) 
                        : searchBST(tree.right, key);
}
```

In Java, there are two BST-based data structures commonly used, *TreeSet* and *TreeMap*. The former implements the set interface, the latter the map interface. 

Some useful methods:
* The iterator returned by iterator() traverses keys in ascending order
* first()/last() will yield the smallest and largest keys in the tree
* lower(12)/higher(3) yeild the largest element strictly less than the argument/smallest element strictly greater than that element
* floor(4.9)/ceiling(5.7) yield the largest leement less than or equal to the argument etc, so the difference is that this allows equality in contrast to lower/higher

### Problems

#### Test if a binary tree satisfies the BST property

* Let's write a program which will take as input a binary tree, and return true if it fulfills the BST property, otherwise false.

```
public static boolean isBST(TreeNode<Integer> tree) {
  return isBSTHelper(tree, Integer.MIN_VALUE, Integer.MAX_VALUE);
}

public static boolean isBSTHelper(TreeNode<Integer> tree, int min, int max) {
  if (tree == null) return true;
  int curData = tree.data;
  if (Integer.compare(curData, min) < 0 || Integer.compare(curData, max) > 0) return false;
  return isBSTHelper(tree.left, min, curData) && isBSTHelper(tree.right, curData, max);
}
```

