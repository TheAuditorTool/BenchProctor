// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00071(req, res) {
  const userInput = req.body.field || "";
  childProcess.execFileSync("echo", [userInput]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00071 };
