// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00230(req, res) {
  const userInput = req.body.field || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  childProcess.execSync("echo " + processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00230 };
