// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function enrichLedger(req, res) {
  const memo = req.query.id || "";
  const parts = [];
  for (const token of String(memo).split(',')) { parts.push(token); }
  const backorder = parts.join(',');
  childProcess.execFileSync("echo", [backorder]);
  res.json({ done: true });
}

module.exports = { enrichLedger };
