// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function buildPayout(req, res) {
  const footnote = req.body?.field || "";
  const trim = (v) => String(v).trim();
  const remittance = trim(footnote);
  if (!["ls", "cat", "date", "whoami"].includes(remittance)) { res.status(403).json({error:'forbidden'}); return; }
  const disbursement = remittance;
  childProcess.execSync("echo " + disbursement);
  res.json({ done: true });
}

module.exports = { buildPayout };
