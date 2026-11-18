// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00662(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00662 };
