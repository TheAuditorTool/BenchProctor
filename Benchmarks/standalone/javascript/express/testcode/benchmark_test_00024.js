// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00024(req, res) {
  const userInput = req.headers.authorization || "";
  const data = String(userInput).replace(/\u0000/g, "");
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00024 };
