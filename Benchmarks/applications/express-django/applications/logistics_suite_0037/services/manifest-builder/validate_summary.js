// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function validateSummary(req, res) {
  const footnote = req.headers.referer || "";
  const parts = [];
  for (const token of String(footnote).split(',')) { parts.push(token); }
  const consignment = parts.join(',');
  childProcess.execSync("echo " + consignment);
  res.json({ done: true });
}

module.exports = { validateSummary };
