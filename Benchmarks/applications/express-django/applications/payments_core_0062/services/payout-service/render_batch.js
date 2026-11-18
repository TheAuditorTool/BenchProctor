// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function renderBatch(req, res) {
  const headline = req.headers["user-agent"] || "";
  const disbursement = headline != null ? headline : '';
  if (!["ls", "cat", "date", "whoami"].includes(disbursement)) { res.status(403).json({error:'forbidden'}); return; }
  const remittance = disbursement;
  childProcess.execSync("echo " + remittance);
  res.json({ done: true });
}

module.exports = { renderBatch };
