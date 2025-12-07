/**
 * Simple Node.js script to demonstrate Dependabot transitive dependency issue.
 * 
 * This uses @dependabot-fixtures packages which are maintained by the Dependabot team
 * specifically for testing transitive dependency scenarios.
 */

const parent = require('@dependabot-fixtures/npm-parent-dependency');

console.log('This project demonstrates Dependabot transitive dependency detection.');
console.log('Using Dependabot test fixture packages to ensure reliable vulnerability detection.');
console.log('Parent package loaded successfully:', parent ? 'OK' : 'FAILED');
