---
layout: page
title: Strings
permalink: /notes/data-structures/strings
---

Strings can be viewed as a special kind of array, which contains only characters.

The following is a function which checks if a string is palindromic (The same forwards and backwards).

```
public static boolean isPalidrome(String s) {
  for (int i = 0, j = s.length() - 1; i < j; ++i, --j) {
    if (s.charAt(i) != s.charAt(j)) {
      return false;
    }
  }
  return true;
}
```

* Strings are immutable in Java, most popular alternative is the Java StringBuilder class
* The key methods that are callable on strings are:
  * charAt(1)
  * compareTo("other")
  * concat("bar")
  * contains("baz")
  * endsWith("xyz")
  * indexOf("needle")
  * indexOf("needle", 12) // starts search at fromIndex, 12
  * lastIndexOf("needle")
  * replace("a", "A")
  * "a,b,c".split(",")
  * startsWith("prefix")
  * substring(1) // can have a beginIdx, and/or endIdx
  * toCharArray()
  * toLowerCase()
  * trim() // removes whitespace from beginning and end

### Problems

#### Interconvert strings and integers

* A string may encode an integer: "123"
* Let's write two functions which support these encodings, one will convert a string to integer, another, integer to string.

```
public static String intToString(int n) {
  boolean isNeg = false;
  if (n < 0) {
    isNeg = true;
  }
  StringBuilder s = new StringBuilder();
  do {
    s.append((char)('0' + Math.abs(n % 10)));
    n /= 10;
  } while (n != 0);
  return s.append(isNeg ? "-" : "").reverse().toString();
}

public static int stringToInt(String s) {
  return (s.charAt(0) == '-' ? -1 : 1) *
    s.substring(s.charAt(0) == '-' ? 1 : 0)
    .chars()
    .reduce(0, (runningSum, c) -> runningSum * 10 + c - '0');
}
```
