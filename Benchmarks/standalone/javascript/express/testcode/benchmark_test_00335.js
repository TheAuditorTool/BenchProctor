// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00335(req, res) {
  const userInput = req.headers.authorization || "";
  const data = Buffer.from(userInput, "hex").toString();
  childProcess.execFileSync("echo", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00335 };
