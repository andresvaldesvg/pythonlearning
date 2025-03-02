// Example 1: Simple if statement
if (5 < 6) {
    console.log("Yes, 5 is less than 6");
    console.log("Everybody knows that");
    console.log("I am a genius");
}

// Example 2: If-else statement
if (10 > 20) {
    console.log("This will not be printed");
} else {
    console.log("10 is not greater than 20");
}

// Example 3: If-elif-else statement
let number = 15;
if (number < 10) {
    console.log("Number is less than 10");
} else if (number === 15) {
    console.log("Number is 15");
} else {
    console.log("Number is greater than 10 but not 15");
}

// Example 4: Nested if statements
let age = 18;
if (age >= 18) {
    console.log("You are an adult");
    if (age >= 65) {
        console.log("You are a senior citizen");
    } else {
        console.log("You are not a senior citizen");
    }
} else {
    console.log("You are not an adult");
}
