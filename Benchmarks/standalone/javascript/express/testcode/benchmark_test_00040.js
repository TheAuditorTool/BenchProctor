// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function BenchmarkTest00040(req, res) {
  const userInput = req.params.id || "";
  const data = decodeURIComponent(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  childProcess.spawn("echo " + processed, { shell: true, stdio: "inherit" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00040 };
