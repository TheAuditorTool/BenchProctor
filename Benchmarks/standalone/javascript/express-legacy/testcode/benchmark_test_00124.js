// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00124(req, res) {
  const userInput = req.headers.referer || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  childProcess.exec("echo " + data, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00124 };
