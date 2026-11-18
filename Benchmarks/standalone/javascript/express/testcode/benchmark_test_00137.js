// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00137(req, res) {
  const userInput = req.params.id || "";
  const data = decodeURIComponent(userInput);
  childProcess.execFileSync("echo", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00137 };
