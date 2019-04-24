---
layout: page
title: Recursion
permalink: /notes/algorithms/recursion
---

The two main components to a recursive algorithm are that a. the algorithm establishes some base case, and b. the algorithm makes progress otherwise, and converges to the base case solution. One type of recursion is divide-and-conquer, however, we don't have to use recursion to solve a divide-and-conquer problem. 

One good use of recursion is the Euclidean algorithm for calculating the greatest common divisor of two numbers. The idea is that for y > x, the GCD of x and y is equal to y - x and x. For example, GCD(156, 36) == GCD(120, 36) == GCD(120, 36) == ... == 12. 

The algo is as follows:

```
public static long GCD(long x, long y) {
  return y == 0 ? x : GCD(y, x % y);
}
```

Notes about recursion:

Recursion is especially suitable when the input is expresed using recursive rules, such as a computer grammar.

Often, the recursive call stack can be mimicked by a stack data structure.

If a function is tail recursive, we don't need a stack at all, just a while loop.

### Problems

#### The Towers of Hanoi Problem

* A peg contains a set of rings in sorted order, with the largest on the bottom. The goal is to transfer these rings from one peg to another.
* You should return a set of paris representing the movements of peg i to beg j, (i, j)

```
private static final int NUM_PEGS = 3;

public static List<List<Integer>> computeTowerHanoi(int numRings) {
  List<Deque<Integer>> pegs = IntStream.range(0, NUM_PEGS)
                                .mapToObj(i -> new ArrayDeque<Integer>())
                                .collect(Collectors.toList());
  for (int i = numRings; i > 0; i--) {
    pegs.get(0).addFirst(i);
  }

  List<List<Integer>> result = new ArrayList<>();
  computeTowerHanoiSteps(numRings, pegs, 0, 1, 2, result);
  return result;
}

public static void computeTowerHanoiSteps(int numRingsToMove, List<Deque<Integer>> pegs, 
                            int fromPeg, int toPeg, int usePeg, List<List<Integer>> result) {
  if (numRingsToMove > 0) {
    computeTowerHanoiSteps(numRingsToMove-1, pegs, fromPeg, usePeg, toPeg, result);
    pegs.get(toPeg).addFirst(pegs.get(fromPeg).removeFirst());
    result.add(List.of(fromPeg, toPeg));
    computeTowerHanoiSteps(numRingsToMove-1, pegs, usePeg, toPeg, fromPeg, result);
  }
}
```

