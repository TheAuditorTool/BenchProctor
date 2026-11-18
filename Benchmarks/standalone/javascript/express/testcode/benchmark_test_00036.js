// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00036(req, res) {
  const userInput = req.cookies.session_token || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  childProcess.execSync("echo " + processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00036 };
