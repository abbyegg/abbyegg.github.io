---
layout: page
title: Greedy Algorithms and Invariants
permalink: /notes/algorithms/greedy
---

### Greedy Algorithms

Greedy algorithms are those which compute a solution in steps, and for each step, the algorithm makes a decision that is locally optimum, and never goes back and changes that selection. This doesn't necessarily produce the optimum overall solution, an example is the coin change problem, which chooses the largest denomination that is smaller than the amount left. (An example is 48 w/ coins of denomination 30, 24, 12, 6, 3, greedy will not get the optimal 24,24 solution.)

* Greedy algorithms are often good choices for optimizations, where there's a natural set of choices to choose from
* It's often easier to conceptualize a greedy algorithm recursively, then implement it using iteration
* Sometimes the correct greedy algorithm isn't obvious, and sometimes it might just give insight into the optimum algorithm

### Invariants

Invariants are conditions which we use to reason about the correctness of a solution. It can be on the values of the variables, or on the control logic. Often, the invariant will be a subset of the input space, for example a subarray.

### Problems

#### The 3-sum problem

* Write an algorithm which takes as input an array and a number, and determines if there are three entries in the array (not necessarily distinct) which add up to the specified number.

```
public static boolean hasTwoSum(List<Integer> arr, int t) {
  int low = 0, high = arr.size()-1;
  while (low <= high) {
    int sum = arr.get(low) + arr.get(high);
    if (sum == t) {
      return true;
    } else if (sum > t) {
      high--;
    } else {
      low++;
    }
  }
  return false;
}

public static boolean hasThreeSum(List<Integer> arr, int t) {
  Collections.sort(arr);
  for (int a : arr) {
    if (hasTwoSum(arr, t - a)) {
       return true;
    }
  }
  return false;
}
```
