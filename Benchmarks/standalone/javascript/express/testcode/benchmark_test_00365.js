// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const nodeUtil = require("util");

async function BenchmarkTest00365(req, res) {
  const userInput = req.params.id || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.execFileSync("echo", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00365 };
