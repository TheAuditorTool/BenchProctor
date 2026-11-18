// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00543(req, res) {
  const userInput = req.body.field || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  childProcess.execSync("echo " + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00543 };
