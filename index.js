/**
 * Simple Node.js script to demonstrate Dependabot transitive dependency issue.
 */

const axios = require('axios');

console.log('This project demonstrates Dependabot transitive dependency detection.');
console.log('Check package.json for the dependency configuration.');

// Simple axios usage
axios.get('https://api.github.com/repos/dependabot/dependabot-core')
  .then(response => {
    console.log(`Repository: ${response.data.name}`);
    console.log(`Stars: ${response.data.stargazers_count}`);
  })
  .catch(error => {
    console.error('Error fetching data:', error.message);
  });
