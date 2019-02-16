---
layout: page
title: Linked Lists
permalink: /notes/data-structures/linked-lists
---

A list implements an ordered collection of values. We typically discuss a *singly linked list*, which contains nodes with only pointers to the next node, and a *doubly linked list*, which contains nodes which have pointers to both the next node and the previous node. The first node is referred to the head of the list, and the last as the tail. The tail's next field is always null. 

The key difference between a list and an array are that the list enables deletion and insertion in time O(1), in contrast w/ the array's insert/delete O(n) time complexity, and obtaining the kth element of a list is O(n) in time, whereas for the array, it is constant.

Example list def:
```
public class ListNode<T> {
  public T data;
  public ListNode<T> next;
}
```

Let's implement a basic list API for find, insertAfter, and deleteAfter:

```
public static ListNode<Integer> searchList(ListNode<Integer> L, int key) {
  if (L != null && L.data != key) {
    L = L.next;
  }
  return L; // if not found, this will be null
}

// insert newNode after node
public static void insertAfter(ListNode<Integer> node, ListNode<Integer> newNode) {
  newNode.next = node.next;
  node.next = newNode;
}

// delete the node after aNode, assumes aNode is not the tail
public static void deleteList(ListNode<Integer> aNode) {
  aNode.next = aNode.next.next;
}
```

* There is also a Java standard linked list library, which can be specified by an ArrayList or LinkedList
* Key methods:
  * add('A') // adds that element to the end of the list
  * add(1, 2, 3) // adds all elements to the end of the list
  * addAll(otherList)
  * clear()
  * contains(4.2)
  * get(12)
  * indexOf(124)
  * isEmpty()
  * iterator() // only forward iteration
  * listIterator() // can travers forward and backward
  * remove(1)
  * removeAll(otherList)
  * retainAll(otherList)
  * set(3, 14)
  * subList(1, 5)
  * toArray()

* We can also utilize the Java Collections class on list collecitons, some useful ones are:
  * Collections.addAll(collection, 1, 2, 3)
  * Collections.binarySearch(list, 24)
  * Collections.fill(list,'f')
  * Collections.swap(list, 0, 1)
  * Collections.reverse(list)
  * Collections.rotate(list, 12)
  * Collections.sort(list), or sort(list, cmp)
* Arrays.asList(1,2,3) is partially mutable, existing entries can be edited, but it cannot be deleted from or added to
* Do not use Arrays.asList(new int[] {1, 2, 3}), you'll get a list of length 1 of type int[], instead use Arrays.asList(new Integer[] {1, 2, 3})
* To preserve the original array, make a copy of it, with Arrays.copyOf(arr, arr.length())

### Problems

#### Merge two sorted lists

* Given two sorted linked lists, we want to combine them in sorted order.

```
public static ListNode<Integer> mergeTwoSortedLists(ListNode<Integer> l1, ListNode<Integer> l2) {
  ListNode<Integer> dummyHead = new ListNode<>();
  ListNode<Integer> head = dummyHead;
  while (l1 != null && l2 != null) {
    if (l1.data <= l2.data) {
      head.next = l1;
      l1 = l1.next;
    } else {
      head.next = l2;
      l2 = l2.next;
    }
    head = head.next;
  }
  if (l1 != null) head.next = l1;
  if (l2 != null) head.next = l2;
  return dummyHead.next;
}
```
