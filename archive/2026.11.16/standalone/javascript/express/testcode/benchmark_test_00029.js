// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00029(req, res) {
  const userInput = req.query.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  childProcess.execSync("echo " + processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00029 };
