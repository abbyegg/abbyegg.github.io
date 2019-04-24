---
layout: page
title: Dynamic Programming
permalink: /notes/algorithms/dynamic-programming
---

Dynamic programming is a general technique for improving the runtime and efficiency of problems which can be decomposed into subproblems. The key here is breaking the problem into subproblems such that a. the subproblems are cached and b. the solution can be found relatively easy given the answer to the subproblems. 

Dynamic programming tips:
* We often use dp for counting and decision problems
* We typically build a cache bottom up rather than recursively for performance reasons
* When DP is implemented recursively, the cache is typically a dynamic structure like a hash table or BST, when implemented iteratively, we use a 1d or 2d array

The classic example is fibonacci, where fib(0) = 0, and fib(1) = 1

```
public static int fib(int n) {
  if (n == 0 || n == 1) return n;
  int x = 0, y = 1, result = 0;
  for (int i = 2; i <= n; i++) {
    result = x + y;
    x = y;
    y = result;
  }
  return y;
}
```

### Problems

#### Find maximum subarray

* Given an array, return the maximum subarray sum

```
public static int findMaxSubarray(List<Integer> arr) {
  int maxSeen = 0, maxEnd = 0;
  for (int a : arr) {
    maxEnd = Math.max(a, maxEnd + a);
    maxSeen = Math.max(maxSeen, maxEnd);
  }
  return maxSeen;
}
```

#### Count the number of score combinations

* In football, a play can lead to 2 points, 3 points, or 7 points.
* Write a program which takes a final score and scores for individual plays, and returns the number of combinations of plays that result in the final score.

```
public static int numCombFinalScore(int finalScore, List<Integer> playScores) {
  int[] combsForScore = new int[playScores.size()][finalScore + 1];
  for (int i = 0; i < playScores.size(); i++) {
    combsForScore[i][0] = 1; // only one way to get to 0
    for (int j = 1; j <= finalScore; j++) {
      int withoutCurPlay = i - 1 >= 0 ? combsForScore[i-1][j] : 0;
      int withCurPlay = j - playScores.get(i) >= 0 ? combsForScore[i][j - playScores.get(i)] : 0;
      combsForScore[i][j] = withoutCurPlay + withCurPlay;
    }
  }
  return combsForScore[playScores.size()-1][finalScore];
}
```
