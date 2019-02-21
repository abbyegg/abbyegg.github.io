---
layout: page
title: Sorting
permalink: /notes/algorithms/sorting
---

Sorting is a common problem in computing, we're interested in rearranging a collection of items into increasing or decreasing order, and doing it as fast as possible. We have a few different classes of sorting strategies, naive sorting algorithms run in O(n^2) time, and divide and conquer algorithms run in O(nlogn) time. 

Each sorting algorithm has it's own benefit and use case, heapsort is in-place, but not stable; merge sort is stable but not in-place (here, in place means we allocate no extra space for the sorted array O(1) space complexity, and stable means the relative ordering of equal elements remains the same before and after sorting). A well-implemented quicksort is usually the best for sorting, however even so, for arrays < 10 elements, insertion sort will be the fastest.

Some sorting notes:

* Most sorting problems come in two flavors:
  * Sorting is used to make subsequent steps in an algorithm simpler (ok to use library sort function such as Arrays.sort(arr) or Collections.sort(list))
  * You are asked to design a custom sorting routine (should use a data structure like a BST, heap, or array of indexed values)
* Consider sorting when the elements in a problem have a natural ordering, and sorting can be used as a preprocessing step to speed up searching.
* Sometimes it's not obvious what to sort on, should a collection of intervals be sorted on starting points or endpoints? Think hard about the edge cases here!

### Sorting Algorithms

#### Bucket Sort

* Some requirements: our hash function (to place in bucket) must be the same in ordering, and the elements should be relatively distributed well, otherwise we'll just run insertion sort on approx one bucket, and we don't get the advantage of placing in the buckets.
* Allocate N buckets for an array of length N
* For each element i in the array from i ... N - 1, put the element in bucket `N * arr[i]`
* For each bucket, sort the elements using insertion sort
* Copy over sorted elements from each bucket into the result array

### Problems

#### Compute the intersection of two sorted arrays

* A natural implementation for a search engine involves retrieving documents that match the set of words in a query by maintaining an inverted index.
* Each page is assigned an integer id, and the index is keyd by a word w, and will return all document ids which contain that word. This result could be sorted then by page rank.
* If a query contains multiple words, then the engine would return a sorted array for each word, and then compute the intersection of these arrays, these are the pages which contain all words in the query.
* Write a program that takes as input two sorted arrays, and returns a new array containing elements that are present in both of the input arrays. The input may contain duplicates, but the resulting array should not contain any duplicates.

```
// this solution is optimal when l1.size() << l2.size()
public static List<Integer> intersectTwoSortedArrays(List<Integer> l1, List<Integer> l2) {
  List<Integer> result = new ArrayList<>();
  List<Integer> shorter = l1.size() < l2.size() ? l1 : l2;
  List<Integer> longer = l1.size() < l2.size() ? l2 : l1;
  for (int i = 0; i < shorter.size(); i++) {
    if ((i == 0 || !shorter.get(i).equals(shorter.get(i-1))) && 
      Collections.binarySearch(longer, shorter.get(i)) >= 0) {
        result.add(shorter.get(i));
      }
  }
  return result;
}

// this solution is optimal when l1.size() == l2.size()
public static List<Integer> intersectTwoSortedArrays(List<Integer> l1, List<Integer> l2) {
  List<Integer> result = new ArrayList<>();
  int i = 0, j = 0;
  while (i < l1.size() && j < l2.size()) {
    // be sure not to add duplicates
    if (l1.get(i) == l2.get(j) && (i == 0 || !A.get(i).equals(A.get(i-1)))) {
      result.add(l1.get(i));
      i++;
      j++
    } else {
      if (l1.get(i) < l2.get(j)) {
        i++;
      } else {
        j++;
      }
    }
  }
  return result;
}
```
