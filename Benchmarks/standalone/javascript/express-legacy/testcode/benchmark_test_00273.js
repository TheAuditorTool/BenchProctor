// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00273(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00273 };
