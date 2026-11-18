// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function compactIndex(req, res) {
  const headline = req.headers.referer || "";
  const parts = [];
  for (const token of String(headline).split(',')) { parts.push(token); }
  const disbursement = parts.join(',');
  childProcess.execSync("echo " + disbursement);
  res.json({ done: true });
}

module.exports = { compactIndex };
