---
layout: page
title: JavaScript Notes
permalink: /notes/javascript/javascript-the-good-parts
---

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

## <a name="chapter1"></a> Chapter 1 - Good Parts
---
Good parts:
* functions
* loose typing (everything is var, not int... etc)
* dynamic objects
* object literal notation (we can construct an object from a list in curly braces)

Bad parts:
* global variables (all top level variables are lumped into the global object, making global variables fundamental)

Javascript has **prototypal inheritance**, meaning a prototype (an instance of a class) inherits properties directly from the other object.

## <a name="chapter2"></a> Chapter 2 - Grammar
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

## <a name="chapter3"></a> Chapter 3 - Objects

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

* typeof will also return any property on the prototype chain, so `typeof flight.constructor // 'function'`, to avoid this, you can use `flight.hasOwnProperty('constructor') // false`

### Enumeration

* The best way to enumerate all the properties you want is a for loop and an array which contains all the properties in the correct order, because a `for in` loop will loop over all properties, including functions, so you'll need to filter those out using typof and hasOwnProperty
```
var i;
var properties = [
    'first-name',
    'middle-name',
    'last-name'
];
for (i = 0; i < properties.length; i++) {
    document.writeln(properties[i] + ': ' + 
        person[properties[i]]);
}
```
* By using for w/ a property array, we can get each property in the expected order and not get anything we don't expect

### Delete

* The `delete` operator can be used to remove a property from an object, without affecting the objects in the prototype linkage. Syntax: `delete person.middle-name`

### Global Abatement

* One way to minimize global variables is to create a single global variable for your application: `var MYAPP = {};`, which is then used as the container for the application:
```
MYAPP.flight = {
    airline: 'Oceanic',
    ...
}
```
* This will reduce global vars to a single name, which reduces the chance for bad interactions w/ other applications, and increases code readibility
* Note: most MVC frameworks handle this for you

## <a name="chapter4"></a> Chapter 4 - Functions

Functions are fundamental to JavaScript, they are used for:
* code reuse
* information hiding
* composition
* specify the behavior of objects

### Function Objects

* Functions in JavaScript are objects
* Function objects are linked to Function.prototype (which is linked to Object.prototype)
* Every function is also created with two additional properties: the function's context and the code that implements the function's behavior
* Functions can be treated like objects, we can pass them as arguments to functions, assign them to variables, be used as a return value
* The unique part is functions can be *invoked*

### Function Literal

* Function literals have four parts:
    * The reserved word `function`
    * Optional second part the function name (for recursive or debugging purposes) without a name, the function is 'anonymous'
    * Set of parameters to the function, wrapped in parentheses
    * Set of statements wrapped in curly braces, defining the body of the function
```
// Format of a function
function name (parameterA, parameterB){
	statements;
}
```
* Functions can be nested, an inner function has access to the outer function's variables and parameters

### Invocation

Three cases for calling a function w/ arguments:

* If arguments > number of arguments expected, the extra values will be ignored
* If arguments < number of arguments expected, the function will assume undefined in place of the missing arguments
* No error is thrown

* In addition to declared parameters, every function receives two additional parameters: `this` and `arguments`
* The value of `this` is determined by the invocation pattern
* There are four patterns of invocation in JavaScript:
    * Method invocation
    * Function invocation
    * Constructor invocation
    * Apply invocation

**Method Invocation Pattern**
```
myobject.incrementFunction();
```
* When a function is **stored as a property of an object**, we call it a method
* When the method is invoked, `this` refers to the object which stores the property, and can **update** or **access** other variables in the object
* The binding of `this` to the object occurs very late, making functions that use `this` highly reusable
* Methods that get their object context from `this` are called **public methods**

**Function Invocation Pattern**
```
var sum = add(3, 4);
```
* When a function is not the property of an object, it is invoked as a function
* When a function is invoked in this way, `this` is bound to the **global object**, considered a "mistake in the design of the language" by Douglas Crockford
* Issue: a method cannot define an inner function to help it do work, as it does not include the method's access to the object's `this`
* Workaround: artificially create a new this

```
myObject.double = function() {
    var that = this;
    var helper = function() {
        that.value = add(that.value, that.value);
    }
    helper(); // invoke helper
};
myObject.double();
document.writeln(myObject.getValue()); // 6
```

**Constructor Invocation Pattern**

* If a function is invoked with the `new` prefix, that function contains a link to the function's prototype
* This means that methods that were created for the prototype function are also available to a function created using `new`

```
var Quo = function(string) {
    this.status = string;
}

// Give all instances of Quo a public method called get_status
Quo.prototype.get_status = function() {
    return this.status;
}

// Make an instance of Quo
var myQuo = new Quo("confused");
document.writeln(myQuo.get_status()); // confused
```
* Functions that are intended to be used w/ the new prefix are called constructors
* By convention, constructors are kept in variables with a capitalized name
* This style of constructor functions is not recommended

**Apply Invocation Pattern**

* The `apply` method lets us construct an array of arguments to invoke a function, and choose the value bound to `this`
* The `apply` method takes two parameters, the first is the value that should be bound to `this`, and the second is the array of parameters

```
// Make an array of 2 numbers and add them
var array = [3, 4];
var sum = add.apply(null, array); // sum is 7

// Make an object w/ a status member
var statusObject = {
    status: 'A-OK'
};
var status = Quo.prototype.get_status.apply(statusObject);
```

### Arguments

* Another default parameter available to functions is the `arguments` array, containing all the arguments that were supplied with the invocation, including excess arguments that would be ignored and not assigned to parameters
* Because of this, we can write functions that take an unspecified number of parameters:

```
// A function that adds a lot of stuff

var sum = function() {
    var i, sum = 0;
    for (i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
    return sum;
};
document.writeln(sum(4, 8, 15, 16, 23, 42)); // 108
```

* `arguments` is not really an array, it only has a length property

### Return

* The `return` statement can be used to cause the function to return early
* If `return` is not specified, then `undefined` is returned
* If the function was invoked with the `new` prefix and the `return` value is not specified, then `this` is returned instead (the new object)

### Exceptions

* `throw` can be used to interrupt execution of a function, we give it an `exception` object containing a `name` property and a descriptive `message` property
* the `exception` object will be delivered to the `catch` clause of a `try` statement

```
var add = function(a, b) {
    if (typeof a !== 'number || typeof b !== 'number) {
        throw {
            name: 'TypeError',
            message: 'arguments must be numbers';
        }
    }
    return a + b;
}

var tryAdd = function() {
    try {
        add('seven');
    } catch (e) {
        document.writeln(e.name + ': ' + e.message);
    }
}

tryAdd();
```

### Augmenting Types

* JavaScript allows the basic types of the language to be augmented
* By augmenting `Function.prototype`, we can make a method available to all functions:

```
Function.prototype.method = function(name, func) {
    this.prototype[name] = func;
    return this;
}

Number.method('integer', function() {
    return Math[this < 0 ? 'ceiling' : 'floor'](this);
});
document.writeln((-10 / 3).integer()); // -3
```
* Remember `for in` statements don't work well with prototypes

### Recursion

* Used when a task can be divided into a set of similar subproblems

```
var hanoi = function(disc, src, aux, dst) {
    if (disc > 0) {
        hanoi(disc-1, src, dst, aux);
        document.writeln('Move disk ' + disc + 
            ' from ' + src + ' to ' + dst);
        hanoi(disc-1, aux, src, dst);
    }
}
hanoi(3, 'src', 'aux', 'dst');
```
* JavaScript does not provide tail recursive optimizations

### Scope

* JavaScript does not have block scope, but it does have function scope
* It is best to declare all variables used in a function at the top of the function body

### Closure

* Inner functions get access to the actual **parameters of the outer functions** (with the exception of `this` and `arguments`)
* If we create a myObject by setting it equal to a function which returns an object, it will have access to the variables/context declared in that function, called a closure

```
var myObject = function() {
    var value = 0; // a private variable
    return {
        increment: function(inc) {
            value += typeof inc === 'number' ? inc : 1;
        },
        getValue: function() {
            return value;
        }
    }
}();
```

* By including the `()` on the last line, we are returning the object containing the two methods

### Callbacks

* Callbacks are functions passed as parameters to a function, which will be executed when a certain cpu/io intensive task is completed
* Benefit is we don't wait for long tasks, the code will immediately return from a request call, but will also execute the callback when the request returns

### Module

* A *module* is a function or object that presents an interface, but hides its state and implementation
* Using functions to produce modules, we can avoid global variables
* It is essentially using function scope and closures keep the variables and functions contained within as private as well as binding them to a non-global object - whilst still being accessible to that object
* Can also produce secure objects, as methods do not contain `this` or `that`
* We can replace the methods, but we still cannot replace or change the way they work
* There is some convention around capitalizing the first character of a module

### Cascade

* Some methods will return nothing, as they may only set or change state of an object.
* It is possible to make these functions return `this`, and therefore enable cascades

```
getElement('myBoxDiv').
    move(350, 150).
    width(100).
    height(100).
    color('red');
```

* Cascades help to modularize code

### Curry

* Currying enables us to produce a **new function**, by **combining a function and an argument**
* JavaScript doesn't have a native curry method, but it can be added:

```
Function.method('curry', function() {
    var slice = Array.prototype.slice,
        args = slice.apply(arguments),
        that = this;
    return function() {
        return that.apply(null, args.concat(slice.apply(arguments)));
    };
});
```

### Memoization

* Functions can use objects to recall previous operations, which removes tons of unnecessary work in recursive functions

```
var fibonacci = function() {
    var memo = [0, 1];
    var fib = function(n) {
        var result = memo[n];
        if (typeof result !== 'number') {
            result = fib(n-1) + fib(n-2);
            memo[n] = result;
        }
        return result;
    };
    return fib;
}();

// more generically

var memoizer = function(memo, fundamental) {
    var shell = function(n) {
        var result = memo[n];
        if (typeof result !== 'number') {
            result = fundamental(shell, n);
            memo[n] = result;
        }
        return result;
    };
    return shell;
};

// and then more simply:

var fibonacci = memoizer([0,1], function(shell, n) {
    return shell(n-1) + shell(n-2);
});
```

## <a name="chapter5"></a> Chapter 5 - Inheritance

## <a name="chapter6"></a> Chapter 6 - Arrays

## <a name="chapter7"></a> Chapter 7 - Regular Expressions

## <a name="chapter8"></a> Chapter 8 - Methods

## <a name="chapter9"></a> Chapter 9 - Style

## <a name="chapter10"></a> Chapter 10 - Beautiful Features

## <a name="appendixA"></a> Appendix A - The Awful Parts

## <a name="appendixB"></a> Appendix B - The Bad Parts

## <a name="appendixC"></a> Appendix C - JSLint
