// 1. Loop
// What is loop?
// Loop is a sequence of instructions that is executed repeatedly until a condition is met.
// Loops are used to repeat a block of code multiple times.

// For loop

// Syntax:
// for (initialization; condition; increment / decrement) {
//     // code to be executed
// }

// Example:

// Print even number from 1 to 100

for (let i = 2; i <= 100; i = i + 2) {
  console.log(i);
}

// Print odd number from 1 to 100 using loop and conditional statement

for (let i = 1; i <= 100; i++) {
  if (i % 2 == 1) {
    console.log(i);
  }
}

// 2. While loop
// What is while loop?
// While loop is a loop that executes a block of code as long as a condition is true.
// While loop is used to repeat a block of code until a condition is met.

// Syntax:

// i = 0
// while (condition) {
//     // code to be executed
//     increment / decrement
// }

// Example:
// Print even number from 1 to 100

let i = 1;
while (i <= 100) {
  if (i % 2 == 0) console.log(i);
  i++;
}

// 2. Function without parameter
// What is function?
// Function is a block of code that performs a specific task and the  block of code will be executed when the function is called.

// Syntax:
// function functionName() {
//     // code to be executed
// }
// functionName();

// Example:

function person1() {
  console.log("Hello, This is me Shakil Khan");
}
person1();

// 3. Function with parameter

function person(name, age) {
  console.log(`My name is ${name}`);
  console.log(`My age is ${age}`);
}
person("Md. Shakil Khan", 27);

//4. Function with return type
//What is return type?
//Return type is the value that is returned by a function.
//Return type is used to pass a value from a function to the calling function.

// example:

function add(a, b) {
  return a + b;
}
console.log(add(5, 20));

// 5. Array
//What is array?
//Array is a collection of values that are stored in a single variable.

//Syntax:
//let arrayName = ["value1", "value2", "value3"];

//Example:
let fruits = ["Apple", "Banana", "Orange"];
console.log(fruits[1]);
