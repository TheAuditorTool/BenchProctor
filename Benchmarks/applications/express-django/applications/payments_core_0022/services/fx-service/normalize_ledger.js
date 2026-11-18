// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function normalizeLedger(req, res) {
  const subject = req.query.id || "";
  const [ledger] = String(subject).split(',');
  childProcess.execSync("echo " + ledger);
  res.json({ done: true });
}

module.exports = { normalizeLedger };
