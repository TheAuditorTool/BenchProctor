// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function collectQuota(req, res) {
  const remark = req.query.id || "";
  const parts = [];
  for (const token of String(remark).split(',')) { parts.push(token); }
  const persona = parts.join(',');
  childProcess.execFileSync("echo", [persona]);
  res.json({ done: true });
}

module.exports = { collectQuota };
