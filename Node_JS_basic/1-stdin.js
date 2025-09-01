// 1-stdin.js
const { rawListeners } = require('process');
const readline = require('readline');

function displayMessage(message) {
  console.log(message);
}

// Create readline interface
const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Display welcome message
displayMessage('Welcome to Holberton School, what is your name?');

// Handle user input for name
rl.question('', (name) => {
  displayMessage(`Your name is: ${name}`);
  rl.close();
});

// Handle process termination - when user ends the program
rl.on('close', () => {
  displayMessage('This important software is now closing') 
});

// Handle SIGNIT (Ctrl+C) gracefully
process.on('SIGNIT', () => {
  displayMessage('\nThis important software is now closing');
  process.exit(0);
})