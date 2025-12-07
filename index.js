/**
 * Simple Node.js script to demonstrate Dependabot transitive dependency issue.
 */

const express = require('express');
const app = express();

console.log('This project demonstrates Dependabot transitive dependency detection.');
console.log('Check package.json for the dependency configuration.');

app.get('/', (req, res) => {
  res.send('Hello World!');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
