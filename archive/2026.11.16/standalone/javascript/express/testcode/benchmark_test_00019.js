// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00019(req, res) {
  const userInput = req.headers.authorization || "";
  const [data] = String(userInput).split(',');
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00019 };
