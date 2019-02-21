---
layout: page
title: Stacks and Queues
permalink: /notes/data-structures/stacks-queues
---

### Stacks

* Stacks support first in, last out semantics for inserts and deletes.
* Supports two basic operations at least, push and pop.
* Don't be afraid to augment the existing stack data structure, such as having a local max variable!

Stacks can be useful to reorder elements, here is a function that uses a stack to print entries of a singly-linked list in reverse order:
```
public static void printListReverse(ListNode<Integer> head) {
  Deque<Integer> nodes = new ArrayDeque<>();
  while (head != null) {
    nodes.add(head.data);
    head = head.next;
  }
  while (!nodes.isEmpty()) {
    System.out.println(nodes.poll());
  }
}
```

* A deque is the preferred way in Java to implement a stack. We can use the deque interface w/ the ArrayDeque which implements this interface, and provides O(1) amortized stack and queue functionality.
* To call only stack methods on the deque, use the following:
  * addFirst(val)
  * peekFirst()
  * removeFirst()
  * descendingIterator()
  * iterator()

### Stack Problems

#### Implement a stack with max API

* Create a stack class that also has max() enabled, which should return the current maximum value in the stack. This method should operate in O(1) time.

```
private static class ElementWithCachedMax {
    public Integer element;
    public Integer max;
    public ElementWithCachedMax(Integer e, Integer m) {
        element = e;
        max = m;
    }
}

public static class Stack {
    private Deque<ElementWithCachedMax> elements = new ArrayDeque<>();

    public boolean empty() {
        return elements.isEmpty();
    }

    public Integer max() {
        return elements.peekFirst().max;
    }

    public Integer pop() {
        return elements.removeFirst().element;
    }

    public void push(Integer val) {
        elements.addFirst(
            new ElementWithCachedMax(val, Math.max(val, empty() ? val : max())));
    }
}

```

### Queues

* Queues support first in, first out semantics for inserts and deletes.
* Tend to be used when we want to preserve order.
* We prefer to use an ArrayDeque for queues as well, the necessary operations are:
  * addLast(12)
  * removeFirst()
  * getFirst() 
  * offerLast(21) // will return false if the enqueue was unsuccessful
  * pollFirst() // return null if empty
  * peekFirst() // return null if empty

#### Implement a queue with max API

```
public class QueueWithNativeMax {
  private Deque<Integer> data = new ArrayDeque<>();

  public void enqueue(Integer x) { data.add(x); }

  public Integer dequeue() { return data.removeFirst(); }

  public Integer max() { return Collections.max(data); }
}
```

