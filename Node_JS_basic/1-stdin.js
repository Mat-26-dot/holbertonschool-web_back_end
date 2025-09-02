#!/usr/bin/env node

// Display welcome message
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Set stdin to readable mode
process.stdin.setEncoding('utf8');

// Handle data input
process.stdin.on('data', (data) => {
  // Remove newline character from input
  const name = data.toString().trim();
  
  // Display the user's name
  process.stdout.write(`Your name is: ${name}\r`);
  
  // Exit the program
  process.exit();
});

// Handle program termination (when user presses Ctrl+C or process ends)
process.on('exit', () => {
  process.stdout.write('This important software is now closing\n');
});

// Handle SIGINT (Ctrl+C)
process.on('SIGINT', () => {
  process.stdout.write('\nThis important software is now closing\n');
  process.exit();
});