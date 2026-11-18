// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00015(req, res) {
  const userInput = req.headers.referer || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.execFileSync("echo", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00015 };
