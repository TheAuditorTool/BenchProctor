// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function summarizeHeader(req, res) {
  const remark = process.env.BILLING_INPUT_0042 || "";
  const remittance = remark != null ? remark : '';
  if (!/^(asc|desc|name|created)$/.test(String(remittance))) { res.status(400).json({error:"invalid"}); return; }
  const dunning = remittance;
  childProcess.execSync("echo " + dunning);
  res.json({ done: true });
}

module.exports = { summarizeHeader };
