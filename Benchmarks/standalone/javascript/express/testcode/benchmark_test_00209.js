// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00209(req, res) {
  const userInput = req.body || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  childProcess.spawn("echo " + data, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00209 };
