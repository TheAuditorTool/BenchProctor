// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00282(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  childProcess.execFileSync("echo", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00282 };
