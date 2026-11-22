// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00306(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00306 };
