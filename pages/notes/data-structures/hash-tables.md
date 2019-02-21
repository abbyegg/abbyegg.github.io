---
layout: page
title: Hash Tables
permalink: /notes/data-structures/hash-tables
---

Hash tables are typically called key-value stores, they have O(1) inserts, lookups, and deletes on average. The underlying idea is we store keys in an array, ie we apply some hash function to get the location of a key in an array. If the hash function is good and we have relatively uniform distribution, lookups, insertions, and deletions all have O(1 + n/m) time complexity, where n is the num of objects, and m is the length of the array. As you can see, it's best when the length of the array is much larger than the number of objects in the hash table. Rehashing a table would be O(n+m), we need to allocate a new array, and then for each object, put it in its new position. We avoid mutable objects as keys.

Good qualities of a hash function are
* It will always put the same object in the same location
* It is easy to compute
* It spreads the objects pretty evenly

Some other notes:
* Can be used as a precomputed lookup table for values, rather than if-then code for mappings.
* When defining your own type that will be put in a hash table, be sure you understand the relationship between **logical equality** and the fields the hash function must inspect.
* Sometimes you'll need a multimap, or a bi-directional map. If the language's standard libraries do not provide that, you can implement it using lists of values.
* Java has both the HashSet and the HashMap, the former stores just keys, the latter key-value pairs. Both do not allow duplicate keys.
  * The order in which keys are traversed by iterator() is unspecified. 
  * HashSet implements retainAll(C), which can be used to perform set intersection, a related method is removeAll(C)
  * For iteration, we'll need to know entrySet(), keySet(), and values()
* The Objects class implements some static utility methods that help with writing equals() and hashCode(), these are:
  * Objects.equals(x, y)
  * Objects.deepEquals(A, B)
  * Objects.hash(42, "Douglas Adams", 3.14, new Date())

An example of a hash function for strings:
```
public static int stringHash(String s, int modulus) {
  final int MULT = 997;
  return s.chars().reduce(0, (val, c) -> (val * MULT + c) % modulus);
}
```

Here is a program that takes as input a set of words, and returns groups of anagrams for those words (each group must contain at least two words). The key insight here, is that for all anagrams, their sorted order is the same!
```
public static List<List<String>> findAnagrams(List<String> dict) {
  Map<String, List<String>> sortedStringToAnagrams = new HashMap<>();
  for (String s : dict) {
    String sorted = 
      Stream.of(s.split("")).sorted().collect(Collectors.joining());
    sortedStringToAnagrams.putIfAbsent(sorted, new ArrayList<String>());
    sortedStringToAnagrams.get(sortedStr).add(s);
  }
  return sortedStringToAnagrams.values()
    .stream()
    .filter(group -> group.size() >= 2)
    .collect(Collectors.toList());
}
```

A hashable class: (ideally we would cache the underlying set and hashcode, rather than generating one each time we compare)
```
public static List<ContactList> mergeContactLists(List<ContactList> contacts) {
  return new ArrayList<>(new HashSet(contacts));
}

public static class ContactList {
  public List<String> names;
  ContactList(List<String> names) { this.names = names; }
  @Override
  public boolean equals(Object obj) {
    if (obj == null || !(obj instanceof ContactList)) {
      return false;
    }
    return this == obj || new HashSet(names).equals(new HashSet(((ContactList)obj).names));
  }
  @Override
  public int hashCode() {
    return new HashSet(names).hashCode();
  }
}
```
### Problems

### Is an anonymous letter constructable?

* Write a program that takes text for an anonymous letter and text for a magazine and determines if it is possible to write the anonymous letter using the magazine.
* The anonymous letter can be written using the magazine, if for each character in the letter, the number of times it appears in the letter is no more than the number of times it appears in the magazine.

```
public static boolean isConstructable(String letterText, String magazineText) {
  // create a map of all the character frequencies in letterText
  Map<Character, Long> charFreqForLetter =
    letterText.chars()
      .mapToObj(c -> (char)c)
      .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
  
  for (char c : magazineText.toCharArray()) {
    if (charFreqForLetter.containsKey(c)) {
      charFreqForLetter.put(c, charFreqForLetter.get(c) - 1);
      if (charFreqForLetter.remove(c, 0L)) {
        charFreqForLetter.remove(c);
        if (charFreqForLetter.isEmpty()) {
          break; // we found all the letters from the magazine
        }
      }
    }
  }
  return charFrequencyForLetter.isEmpty();
}
```
