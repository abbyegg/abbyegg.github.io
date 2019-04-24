# Notes on Javascript the Good Parts

## Table of Contents
* [Chapter 1 - Good Parts](#chapter1)
* [Chapter 2 - Grammar](#chapter2)
* [Chapter 3 - Objects](#chapter3)
* [Chapter 4 - Functions](#chapter4)
* [Chapter 5 - Inheritance](#chapter5)
* [Chapter 6 - Arrays](#chapter6)
* [Chapter 7 - Regular Expressions](#chapter7)
* [Chapter 8 - Methods](#chapter8)
* [Chapter 9 - Style](#chapter9)
* [Chapter 10 - Beautiful Features](#chapter10)
* [Appendix A - the Awful Parts](#appendixA)
* [Appendix B - the Bad Parts](#appendixB)
* [Appendix C - JSLint](#appendixC)

## <a name="chapter1"/></a> Chapter 1 - Good Parts
---
Good parts:
* functions
* loose typing (everything is var, not int... etc)
* dynamic objects
* object literal notation (we can construct an object from a list in curly braces)

Bad parts:
* global variables (all top level variables are lumped into the global object, making global variables fundamental)

Javascript has **prototypal inheritance**, meaning a prototype (an instance of a class) inherits properties directly from the other object.

## <a name="chapter2"/></a> Chapter 2 - Grammar
---

* Almost all whitespace is flexible, however there is a need to have at least one whitespace character between tokens.
* block commenting syntax like `/* */` is not always safe to use, because regular expressions contain these characters, so it's best to use // always.

### Numbers
* There is only one number type, 64 bits, same as Java's `double`.
* `NaN` is the result of bad numeric operations
* `typeOf(NaN) === Number` is true
* use `isNaN(x)` to check for this value

### Strings
* 16-bit character set and don't have character types
* Can use single or double quotes for string literals
* Like Java, strings are **immutable** and have a length property

### Statements
* `var` when used in a function defines the function's private variables
* *switch*, *for*, *while*, *do* statements have an optional `label` prefix which can be applied to allow for control over which statement to break or continue.

```
loop1 :
for (int i = 0; i < 3; i++) {
    loop2 :
    for (int j = 0; j < 5; j++) {
        if (i == 1 && j == 1) {
            continue loop1;
        }
    }
}
```

* Blocks do NOT create a new scope in Javascript, so variables should be defined at the top of the function, rather than in the blocks.
* `var` is function scoped, and `let` is block scoped.
* `const` is also block scoped, and will throw an error if that variable is attempted to be changed.

Falsey values:
* `false`
* `null`
* `undefined`
* the empty string ''
* the number 0
* the number NaN

All other values are truthy

* When using a "for in" loop, usually a good idea to use `hasOwnProperty(variable)` to make sure the property belongs to the object you want and is not instead an inherited property from the prototype chain:

```
for (myvariable in object) {
    if (object.hasOwnPropery(myvariable)) {
        ... // statements to be executed
    }
}
```

* like Java, a do while statement is always executed at least once
* A `try` statement will catch any code that throws an exception in the block, the `catch` clause defines the new variable which catches the exception
* If the `return` expression is not specified, then the return value === undefined
* `break` exits the statement, and `continue` forces the next iteration of the loop, both with an optional *label* as mentioned above

### Expressions

* A ternary expression follows `exp ? val1 : val2;`, where if exp is truthy, we execute val1, otherwise val2
* An *invocation* is (expression 1, expression 2)
* *refinement* is either .name or [expression] as used in an array

## <a name="chapter3"/></a> Chapter 3 - Objects

* Everything besides numbers, strings, booleans, null and undefined are objects, including arrays and functions
* Objects are class-free
* Inheritance can be achieved through prototypal inheritance, which can reduce object init time and memory consumption

### Object Literals

* An object literal is a set of curly braces around zero or more name/value pairs
* The quotes around an object property's name are optional if the name would be legal Javascript and not a reserved word 

```
var empty_object = {};

var stooge = {
    'first-name': 'Jerome',
    'last-name': 'Howard'
};
```

* `undefined` will be returned a nonexistent member is accessed, and the `||` operator can be used to fill in default values

### Retrieval 

* Value can be retrieved from an object using [ ] notation, or if it is a legal Javascript name, then the . notation can be used, which is preferred

### Update

* A value can be updated by assignment, if the name already exists, the property will be replaced if we do `stooge['first-name'] = 'jerome';`
* An object is augmented if the name does not exist

### Reference

* Objects are passed by reference, never by value

### Prototype

* Every object has a prototype object from which it can inherit properties, so if it's an object literal, it's linked to `Object.prototype`, which can be considered the 'root parent'
* The prototype chain/link is only used for retrieval
* If an object does not have a property you ask it for, it will keep looking up the prototype chain until it finds it, if the property does not exist anywhere in the chain it will return undefined
* The prototype relationship is dynamic, if you update a parent prototype by adding a property, that will be accessible by any objects based on that prototype

### Reflection

* `typeof` can be used to identify if an object contains a certain property

```
var flight = {
    airline: "Oceanic", 
    number: 815, 
    departure: {
        IATA: "SYD",
        time: "2004-09-22 14:55",
        city: "Sydney" }, 
    arrival: {
        IATA: "LAX",
        time: "2004-09-23 10:42",
        city: "Los Angeles" 
    }
};
typeof flight.number // 'number'
typeof flight.arrival // 'object'
typeof flight.manifest // 'undefined'
```



## <a name="chapter4"/></a> Chapter 4 - Functions

## <a name="chapter5"/></a> Chapter 5 - Inheritance

## <a name="chapter5"/></a> Chapter 6 - Arrays

## <a name="chapter5"/></a> Chapter 7 - Regular Expressions

## <a name="chapter5"/></a> Chapter 8 - Methods

## <a name="chapter5"/></a> Chapter 9 - Style

## <a name="chapter5"/></a> Chapter 10 - Beautiful Features

## <a name="appendixA"/></a> Appendix A - The Awful Parts

## <a name="appendixB"/></a> Appendix B - The Bad Parts

## <a name="appendixC"/></a> Appendix C - JSLint
