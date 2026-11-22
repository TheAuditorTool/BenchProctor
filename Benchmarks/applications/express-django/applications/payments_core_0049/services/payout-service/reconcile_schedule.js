// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function reconcileSchedule(req, res) {
  const headline = req.query.id || "";
  const parts = [];
  for (const token of String(headline).split(',')) { parts.push(token); }
  const disbursement = parts.join(',');
  childProcess.execFileSync("echo", [disbursement]);
  res.json({ done: true });
}

module.exports = { reconcileSchedule };
