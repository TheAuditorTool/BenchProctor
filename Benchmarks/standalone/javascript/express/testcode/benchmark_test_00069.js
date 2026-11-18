// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00069(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  childProcess.execFileSync("echo", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00069 };
