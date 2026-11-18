// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00556(req, res) {
  const userInput = req.params.id || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00556 };
