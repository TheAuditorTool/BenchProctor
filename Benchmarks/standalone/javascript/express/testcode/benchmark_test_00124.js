// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00124(req, res) {
  const userInput = req.headers.referer || "";
  const data = `${userInput}`;
  childProcess.execFileSync("echo", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00124 };
