---
layout: page
title: Searching
permalink: /notes/algorithms/searching
---

Search algorithms are typically run on static data stored in sorted order in an array. We can look at both binary search and general search.

### Binary Search

The basic idea is to eliminate half of the possible keys to check on every iteration, until we've found the target or it doesn't exist. Runs in O(logn) time.
The following is a correct implementation of this algorithm:

```
public static int bsearch(int target, List<Integer> list) {
  int lo = 0, hi = list.size() - 1;
  while (lo <= hi) {
    int mid = lo + ((hi - lo) / 2);
    if (list.get(mid) == target) {
      return mid;
    } else if (list.get(mid) < target) {
      lo = mid + 1;
    } else {
      hi = mid - 1;
    }
  }
  return -1;
}
```

Java knows how to compare built in types, however, we need to provide a comparator for user-defined types. The following is an example of how to go about searching a collection of custom objects:

```
public static class Student {
  public String name;
  public double gpa;
  public Student(String name, double gpa) {
    this.name = name;
    this.gpa = gpa;
  }
}

private static final Comparator<Student> compGPA = (a, b) -> {
  if (a.gpa == b.gpa) return a.name.compareTo(b.name);
  return Double.compare(b.gpa, a.gpa);
};

public static boolean studentFound(List<Student> students, Student target, Comparator<Student> compGPA) {
  return Collections.binarySearch(students, target, compGPA) >= 0;
}
```

Some more Java-specific notes:

* For Java, we can call contains(ele) on an ArrayList, LinkedList, HashSet, and TreeSet, with very different time complexities.
* To search an array, use Arrays.binarySearch(arr, "euler").
* To search a sorted List-type object, use Collections.binarySearch(list, 24).
* The time complexity depends on the nature of the list implementation. For linked lists, this is O(n), rather than the optimized O(logn) for array-like structures.
* These binarySearch methods don't guarantee the value returned when duplicates exist.
* If the search target isn't present, binarySearch will return (-(insertion point) - 1), so a negative value nonetheless

### Problems

#### Search a sorted array for first occurence of k

* Binary search commonly asks for the index of *any* element of a sorted array that is equal to the target. Let's write a function that will always return the first of such elements, if one exists.
* Assume we start with a sorted array, and return either the index of the first element matching the target, or -1.

```
public static int searchFirstOfK(List<Integer> arr, int k) {
  int left = 0, right = arr.size() - 1;
  int result = -1;
  while (left <= right) {
    int mid = left + ((right - left) / 2);
    if (arr.get(mid) > k) {
      right = mid - 1;
    } else if (arr.get(mid) == k) {
      result = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return result;
}
```

### Generalized Search

These problems do not use binary search, rather, they rely on tradeoffs between RAM and computation time, avoid wasted comparisons when searching for the min and max simultaneously, use randomization, bit-level manipulations, and more!

WIP 
