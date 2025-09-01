// 1-stdin.js
function displayMessage(message) {
  process.stdout.write(message + '\n');
}

// Display welcome message
displayMessage('Welcome to Holberton School, what is your name?');

// Handle stdin data
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  displayMessage(`Your name is: ${name}`);
  process.exit(0);
});

// Handle process termination
process.on('SIGINT', () => {
  displayMessage('This important software is now closing');
  process.exit(0);
});

process.on('exit', () => {
  displayMessage('This important software is now closing');
});

