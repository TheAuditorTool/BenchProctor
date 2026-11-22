// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00343(req, res) {
  const userInput = req.headers.referer || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  childProcess.exec("echo " + data, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00343 };
