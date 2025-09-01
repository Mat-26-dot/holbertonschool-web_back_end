// 1-stdin.js
const readline = require('readline');

function displayMessage(message) {
  console.log(message);
}

// Create readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

// Display welcome message
displayMessage('Welcome to Holberton School, what is your name?');

// Listen for line input
rl.on('line', (input) => {
  displayMessage(`Your name is: ${input}`);
  rl.close();
});

// Handle close event
rl.on('close', () => {
  displayMessage('This important software is now closing');
  process.exit(0);
});

// Handle SIGINT (Ctrl+C) gracefully
process.on('SIGINT', () => {
  displayMessage('\nThis important software is now closing');
  process.exit(0);
});
