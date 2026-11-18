// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const nodeUtil = require("util");

async function BenchmarkTest00063(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const data = nodeUtil.format("%s", userInput);
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00063 };
