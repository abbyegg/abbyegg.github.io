---
layout: page
title: Heaps
permalink: /notes/data-structures/heaps
---

Heaps are a special kind of binary tree, which are always complete as a rule, and where each key satisfies the heap property, meaning every key is at least as big as it's children (or for a min heap this is reverse). Many implementations use an array to store data in the heap, such that for each node at position i, the left child can be found at 2i + 1, and right child can be found at 2i + 2. Max heaps support O(logn) insertion (we insert at the end, and then bubble up if needed). Another word for a heap is a priority queue, because it behaves similar to a queue, with one difference, each element is stored related to its priority, and deletion will remove the value of highest priority.

Heaps are implemented in the Java PriorityQueue class.

Some key methods are pQueue.add(“val”), pQueue.peek(), pQueue.poll(), they all return null if the collection is empty.

Here is a function that shows how simple it is to use a heap to store things like the k longest strings so far:
```
public static List<String> topK(int k, Iterator<String> iter) {
  PriorityQueue<String> minHeap = new PriorityQueue<>(
    k, (s1, s2) -> Integer.compare(s1.length(), s2.length())); // will order from shortest to longest
  while (iter.hasNext()) {
    String nextStr = iter.next();
    // we should insert if we don't have k values yet 
    // or if the new string is longer than the current min
    if (minHeap.size() < k || nextStr.length() > minHeap.peek().length()) {
      minHeap.add(nextStr);
      if (minHeap.size() > k) {
        minHeap.poll();
      }
    }
  }
  return new ArrayList<>(minHeap);
}
```
* In the above example, each string is processed in O(logk) time, which is the time to add and remove the minimum element from the heap. Therefore, the total time complexity for n strings is O(nlogk) time.


### Problems

#### Merge sorted files

* Let's say we have 500 files containing sorted data, and the data needs to be combined in sorted order.
* Key insight here is that for each of the files, we just need to look at the first value and compare to all other first values to know which comes next.

```
private static class ArrayEntry {
  public int value;
  public int arrId;
  public ArrayEntry(int v, int a) {
    value = v;
    a = arrId;
  }
}

public static List<Integer> mergeSortedArrays(List<List<Integer>> sortedArrays) {
  List<Iterator<Integer>> iters = new ArrayList<>(sortedArrays.size());
  for (List<Integer> arr : sortedArrays) {
    iters.add(arr.iterator());
  }
  PriorityQueue<ArrayEntry> heap = new PriorityQueue<>(
    sortedArrays.size(), (o1, o2) -> Integer.compare(o1.value, o2.value));
  for (int i = 0; i < iters.size(); i++) {
    if (iters.get(i).hasNext()) {
      heap.add(new ArrayEntry(iters.get(i).next(), i));
    }
  }
  List<Integer> result = new ArrayList<>();
  while (!heap.isEmpty()) {
    ArrayEntry nextMin = heap.poll();
    result.add(nextMin.value);
    if (iters.get(nextMin.arrId).hasNext()) {
      heap.add(new ArrayEntry(iters.get(nextMin.arrId).next()), nextMin.arrId);
    }
  }
  return result;
}
```
