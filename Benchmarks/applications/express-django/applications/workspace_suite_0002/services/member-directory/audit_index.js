// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function auditIndex(req, res) {
  const transcript = req.headers.referer || "";
  const parts = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const heading = parts.join(',');
  childProcess.execSync("echo " + heading);
  res.json({ done: true });
}

module.exports = { auditIndex };
