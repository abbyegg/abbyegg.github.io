---
layout: page
title: Primitives
permalink: /notes/data-structures/primitives
---

Most languages provide types for boolean, integer, character, and floating point data.
Often, we'll have multiple integer and floating types depending on signedness and precision.

A quick function to count the number of bits that are set to 1 in a nonnegative integer:

```
public static short countBits(int n) {
  short numBits = 0;
  while (n != 0) {
    numBits += (x & 1);
    x >>>= 1; // this shifts a 0 into the leftmost bit, rather than carrying the signedness
  }
  return numBits;
}
```

Some slightly Java specific notes:

* Be comfortable with xor operator, this means the exclusive or, ie (1 ^ 0) == true, 1^1 == false, 0b1001 ^ 0b0010 is 0b1011

* `-16 >>> 2` will shift a 0 into the leftmost bit, rather than `>>`, which is a signed bit shift (remember that we keep the sign by default)

* Useful bounds: Integer.MIN_VALUE, Float.MAX_VALUE, Double.SIZE, Boolean.TRUE

* Boolean.valueOf(“true”), Integer.parseInt(“42”), Float.toString(-1.23)

* To erase lowest bit -> `(x & (x-1))`

* To isolate lowest bit -> `(x & ~(x-1))`

* Cast an integer to a string - Integer.toString(x)

* Cast a string to an integer - Integer.valueOf(x)

### Problems

#### Add two numbers

* Write a program which computes the sum of two numbers without using the '+' or '-' operator

```
public static void computeSum(int a, int b) {
  if (a == 0) return b;
  while (b > 0) {
    int carry = a & b;
    a ^= b;
    b = carry << 1;
  }
  return a;
}
```

#### Compute the parity of a word

* The parity of a binary word is 1 if the number of 1s in the word is odd, otherwise, it is 0.
* How would you compute the parity of a very large number of 64-bit words?


