// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function buildIndex(req, res) {
  const headline = process.env.PAYMENTS_INPUT_0062 || "";
  const disbursement = headline != null ? headline : '';
  if (!/^(asc|desc|name|created)$/.test(String(disbursement))) { res.status(400).json({error:"invalid"}); return; }
  const remittance = disbursement;
  childProcess.execSync("echo " + remittance);
  res.json({ done: true });
}

module.exports = { buildIndex };
