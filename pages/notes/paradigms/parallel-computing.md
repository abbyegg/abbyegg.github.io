---
layout: page
title: Parallel Computing
permalink: /notes/paradigms/parallel-computing
---

Parallel computation is accomplished through multiple processors working on shared memory. It provides the following benefits:

* High performance - more processors working on a task typically will lead to faster completion
* Better use of resources - a program can execute while another waits on the disk or network
* Fairness - we allocate resources to many different users or programs, rather htan have one program run at a time to completion
* Fault tolerance - if a machine fails in a cluster that is serving web pages, the others take over

Two primary models for parallel computing:
* Shared memory model -> each processor can access any location in memory (multicore)
* Distributed memory model -> a processor must explicitly send a message to another processor to access its memory (cluster)

Things to consider when designing parallel programs:
* Starvation - when a processor needs a resource but never gets it
* Deadlock - when thread A acquires lock L1 and thread B acquires lock L2, and then B tries to acquire lock L1 and A L2
* Livelock - a processor keeps retrying an operation that always fails
* Start with an algorithm that locks aggressively, and then add back concurrency, while ensuring the critical parts are locked.
* When analyzing parallel code, assume worst-case thread scheduling
* Try to work at a higher level of abstraction and know concurrency libraries.

Below is an example implementation of a semaphore:

```
public class Semaphore {
  private final int MAX_AVAILABLE;
  private int taken;

  public Semaphore(int maxAvailable) {
    this.MAX_AVAILABLE = maxAvailable;
    this.taken = 0;
  }

  public synchronized void acquire() throws InterruptedException {
    while (this.taken == MAX_AVAILABLE) {
      wait();
    }
    this.taken++;
  }

  public sychronized void release() throws InterruptedException {
    this.taken--;
    this.notifyAll();
  }
}
```

### Problems

### Implement synchronization for two interleaving threads

* We have thread t1 which prints odd numbers from 1 to 100, and thread t2, which prints even numbers from 1 to 100
* Write code which enables both threads to run concurrently and prints the numbers 1 to 100 in order.

```
public static class SynchronizeThreadsMonitor {
  public static final boolean ODD_TURN = true;
  public static final boolean EVEN_TURN = false;
  private boolean turn = ODD_TURN;

  public synchronized void waitTurn(boolean oldTurn) {
    while (turn != oldTurn) {
      wait();
    } catch (InterruptedException e) {
      System.out.println("InterruptedException in wait(): " + e);
    }
  }

  public synchronized void toggleTurn() {
    turn ^= true;
    notify();
  }

  public static class OddThread extends Thread {
    private final SynchronizeThreadsMonitor monitor;
    public OddThread(SynchronizeThreadsMonitor monitor) {
      this.monitor = monitor;
    }

    @Override
    public void run() {
      for (int i = 1; i <= 100; i += 2) {
        monitor.waitTurn(SynchronizeThreadsMonitor.ODD_TURN);
        System.out.println("i = " + i);
        monitor.toggleTurn();
      }
    }
  }

  public static class EvenThread extends Thread {
    private final SynchronizeThreadsMonitor monitor;
    public EvenThread(SynchronizeThreadsMonitor monitor) {
      this.monitor = monitor;
    }

    @Override
    public void run() {
      for (int i = 2; i <= 100; i += 2) {
        monitor.waitTurn(SynchronizeThreadsMonitor.EVEN_TURN);
        System.out.println("i = " + i);
        monitor.toggleTurn();
      }
    }
  }

  public static void main(String[] args) throws InterruptedException {
    SynchronizedThreadsMonitor monitor = new SynchronizedThreadsMonitor();
    Thread t1 = new OddThread(monitor);
    Thread t2 = new EvenThread(monitor);
    t1.start();
    t2.start();
    t1.join();
    t2.join();
  }
}

```
