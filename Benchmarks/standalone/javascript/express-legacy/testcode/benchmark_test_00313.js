// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00313(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!["ls", "cat", "date", "whoami"].includes(data)) { res.status(403).json({error:'forbidden'}); return; }
  const allowedBin = data;
  childProcess.spawn("echo " + allowedBin, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00313 };
