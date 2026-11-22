// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00304(req, res) {
  const userInput = req.body.field || "";
  const data = String(userInput).replace(/\u0000/g, "");
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00304 };
