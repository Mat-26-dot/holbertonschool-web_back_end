#!/usr/bin/env node

// Display welcome message
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Set stdin to readable mode
process.stdin.setEncoding('utf8');
process.stdin.resume();

// Handle data input
process.stdin.on('data', (data) => {
  // Remove newline character from input
  const name = data.toString().trim();
  
  // Display the user's name
  process.stdout.write(`Your name is: ${name}\r`);
});

// Handle end of input
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});

// Handle SIGINT (Ctrl+C)
process.on('SIGINT', () => {
  process.stdout.write('\nThis important software is now closing\n');
  process.exit();
});