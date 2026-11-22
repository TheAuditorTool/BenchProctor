// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const nodeUtil = require("util");

async function BenchmarkTest00312(req, res) {
  const userInput = req.body.payload || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.exec("echo " + data, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00312 };
