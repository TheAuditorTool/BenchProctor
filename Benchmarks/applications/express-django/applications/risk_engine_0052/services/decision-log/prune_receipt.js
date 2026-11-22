// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function pruneReceipt(req, res) {
  const memo = req.query.id || "";
  const parts = [];
  for (const token of String(memo).split(',')) { parts.push(token); }
  const verdict = parts.join(',');
  childProcess.execFileSync("echo", [verdict]);
  res.json({ done: true });
}

module.exports = { pruneReceipt };
