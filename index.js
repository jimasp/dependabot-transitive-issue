/**
 * Simple Node.js script to demonstrate Dependabot transitive dependency issue.
 */

const async = require('async');

console.log('This project demonstrates Dependabot transitive dependency detection.');
console.log('Check package.json for the dependency configuration.');

// Simple async usage
async.map([1, 2, 3], (num, callback) => {
  setTimeout(() => {
    callback(null, num * 2);
  }, 100);
}, (err, results) => {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log('Doubled array:', results);
  }
});
