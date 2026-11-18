// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00034(req, res) {
  const userInput = req.headers.authorization || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00034 };
