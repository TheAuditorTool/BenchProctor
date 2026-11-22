// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00273(req, res) {
  const userInput = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  childProcess.exec("echo " + data, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00273 };
