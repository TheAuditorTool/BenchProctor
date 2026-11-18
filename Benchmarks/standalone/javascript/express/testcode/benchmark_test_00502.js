// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00502(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00502 };
