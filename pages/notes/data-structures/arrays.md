---
layout: page
title: Arrays
permalink: /notes/data-structures/arrays
---

A contiguous block of memory. Retrieving and updating A[i] takes O(1) time. Insertion into a full array is handled by resizing the array by allocating a new array with double the size and copying over all the elements into it. Deleting an element means we have to move all elements over by one, same with inserting into the middle.

A function which reorders the elements such that all even entries appear first:

```
public static void evenOdd(List<Integer> arr) {
  int nextEven = 0, nextOdd = arr.size()-1;
  while (nextEven < nextOdd) {
    if (arr.get(nextEven) % 2 == 0) {
      nextEven++;
    } else {
      Collections.swap(arr, nextEven, nextOdd);
      nextOdd--;
    }
  }
}
```

Some notes about array problems:

* Array problems often have brute force solutions which use O(n) space, but many times we can do the operation in-place to achieve O(1) space.
* Filling an array from the front is slow, try to fill from the back.
* Consider processing an array from the back when dealing with integers encoded by an array, or reverse the array so we have the least-significant digit at the front.
* To create a new array, `new int[] {1, 2, 3}`
* To create a new 2d array, `new Integer[3][]`, this creates an array which will hold three rows, each of these must be explicitly assigned
* The **Arrays** class consists of many useful static utility methods
  * asList()
  * binarySearch(arr, 213)
  * copyOf(arr)
  * copyOfRange(arr, 1, 5)
  * equals(arr1, arr2)
  * fill(arr, 42)
  * sort(arr) (or to overload the comparator sort(arr, cmp))
  * toString()

### Problems

#### The Dutch national flag problem

* The quicksort algorithm is recursive and relies on the fast in-place 'pivot' method, which will reorder the array such that all elements less than or equal to the pivot come before all elements greater than the pivot
* However, with a naive implementation, the algorithm can have large runtimes and deep call stacks on arrays with many duplicates, because the subarrays might differ greatly in size
* The Dutch national flag partitioning is to reorder the elements such that all before the pivot appear first, all equal next, and all greater than last.

```
public static void dutchFlagPartition(int pivotIndex, List<Integer> arr) {
  int less = 0;
  int equal = 0;
  int greater = arr.size();
  int pivot = arr.get(pivotIndex);

  while (equal < greater) {
    int cur = arr.get(equal);
    if (cur < pivot) {
      Collections.swap(arr, less++, equal++);
    } else if (cur == pivot) {
      ++equal;
    } else {
      Collections.swap(arr, equal, --greater);
    }
  }
}
```

#### Buy and sell a stock once

* Consider an array representing a sequence of stock prices, let's design an algorithm that takes in this array, and determines the maximum profit that can be made by buying and selling the share over a day range, subject to the constraint that the sell must come after the buy, and they have to be made on different days.

```
public static int computeMaxProfit(List<Double> prices) {
  double minPrice = Double.MAX_VALUE, double maxProfit = 0;
  for (double price : prices) {
    maxProfit = Math.max(maxProfit, price-minPrice);
    minPrice = Math.min(minPrice, price);
  }
  return maxProfit;
}
```
