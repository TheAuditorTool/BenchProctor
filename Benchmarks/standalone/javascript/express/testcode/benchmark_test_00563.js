// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00563(req, res) {
  const userInput = req.body.payload || "";
  const [data] = String(userInput).split(',');
  childProcess.execFileSync("echo", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00563 };
