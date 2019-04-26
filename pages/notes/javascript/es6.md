---
layout: page
title: JavaScript ES6 Notes
permalink: /notes/javascript/es6
---

ES6 is also known as EMCAscript 2015, and is a major update to the language. 

The following is an overview of some of the new features that can be leveraged in ES6, it should be kept in mind that we will still need to have polyfills and make sure that any code will run in many browsers, which may not implement ES6.

### Let and Const

* New keywords added by ES6 `const` and `let`
* `const` is immutable, best practice to define these variables w/ all uppercase characters
* `let` is block-scoped (`var` is only function or global scoped)

### Hoisting and Variables

* In JavaScript, a variable can be used before it is declared, because JavaScript uses 'hoisting' to bring all variables to the top of the current scope.
* Note: declarations, NOT initializations are hoisted, so adding `var x = 5`, and then using `x` earlier in the function will not work.

```
x = 5;
console.log(x); // 5
var x;
```

* The keywords `let` and `const` are not hoisted
* All variables should be declared before they are used

### Functions

**Arrow Functions**

Two factors influenced introducing arrow functions: shorter functions and no `this` keyword

* Arrow functions simplify binding to the `this` keyword, it does not have it's own `this` based on how it's called, it inherits the `this` of the enclosing lexical scope
* Cannot be used as constructors, and do not make good methods because they will not inherit the object's context as `this`

Syntax:

```
// Basic
(param1, param2, ...) => { statements }

(param1, param2, ...) => expression
// equivalent to: => { return expression; }

// Parentheses are optional when there's only one param name:
param1 => { statements }

// No params:
() => { statements; }

// Advanced
// Parenthesize the body to return an object literal:
params1 => ({foo: bar})

// rest params
(param1, param2, ...rest) => { statements }

// default params
(param1 = 1, param2 = 2) => { statements }

// destructuring in the param list
var f = ([a, b] = [1, 2], {x: c} = {x: a + b}) => a + b + c;
f(); // 6
```

* The methods `call` and `apply` cannot pass in `this`, they can only pass in parameters for arrow functions
* Similarly w/ how arrow functions get their `this` from the enclosing scope, `arguments` also comes from the enclosing scope
* With the concise body syntax, a return statement is unnecessary, however, it must be included in a block body
* Remember to wrap object literals in `()` parentheses!

```
var func = x => x * x;                  
// concise body syntax, implied "return"

var func = (x, y) => { return x + y; }; 
// with block body, explicit "return" needed
```

* Can create 'Immediately Invoked Function Expressions' through the syntax `(() => 'foobar')();`, which returns "foobar"

**Rest Parameters**

* A function's last parameter can be prefixed with `...` which causes all remaining user-supplied arguments to be placed in a standard JavaScript array
* **Only** the last param can be a rest param, and it can have any name

Syntax:

```
function f(a, b, ...theArgs) {
  // ...
}

function myFun(a, b, ...manyMoreArgs) {
  console.log("a", a); 
  console.log("b", b);
  console.log("manyMoreArgs", manyMoreArgs); 
}

myFun("one", "two", "three", "four", "five", "six");

// Console Output:
// a, one
// b, two
// manyMoreArgs, [three, four, five, six]
```

* The rest param differs from the arguments object in that the rest params only contains the extra arguments, and the arguments array is not a real array, whereas the rest array is

**Spread Syntax**

* Allows an iterable such as an array expression or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected

Syntax:

```
// for function calls
myFunction(...iterableObj);

// for array literals or strings
[...iterableObj, 5, 'one']

// for object literals (EMCAscript 2018)
let objClone = { ...iterableObj };
```

### 'For of' loop

```
let nums = [1, 2, 3];

for (let num of nums) {
    console.log(num);
}
```

### Template Literals

* Useful for capturing whitespace as well as string interpolation of variables
* Between the curly braces must return a string, but can be code

```
let name = 'Abby';
let description = `
    Check this out! My name is ${name}!
`;
```

### Destructuring

**Destructuring Arrays**

* Simplifies syntax for getting variables in iterables
* Must be requested by position!

```
let nums = [1, 2, 3];
let [a, b] = nums;

// or...
let [a, , b] = nums;

// can be used to swap numbers
let a = 1;
let b = 2;
[b, a] = [a, b];
```

* Can also set default values for the destructuring syntax
* Name must correspond to the name in the object, however, can use an alias like `let {name1, greet: hello}` to refer to the function as `hello` instead

**Destructuring Objects**

```
let obj = {
    name: 'Abby',
    greet: function() {
        console.log('Hello');
    }
};
let {name1, greet} = obj;

greet(): // prints 'Hello'
```
