// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const nodeUtil = require("util");

async function BenchmarkTest00321(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00321 };
