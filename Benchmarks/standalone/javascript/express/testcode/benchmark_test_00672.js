// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00672(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = Buffer.from(userInput, "hex").toString();
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00672 };
