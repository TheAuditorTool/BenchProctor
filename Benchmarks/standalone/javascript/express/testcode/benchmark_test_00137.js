// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00137(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = decodeURIComponent(userInput);
  if (!["ls", "cat", "date", "whoami"].includes(data)) { res.status(403).json({error:'forbidden'}); return; }
  const allowedBin = data;
  childProcess.execSync("echo " + allowedBin);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00137 };
