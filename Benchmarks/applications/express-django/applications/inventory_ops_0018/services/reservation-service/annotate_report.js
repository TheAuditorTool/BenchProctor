// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function annotateReport(req, res) {
  const transcript = req.headers.referer || "";
  const parts = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const backorder = parts.join(',');
  childProcess.execSync("echo " + backorder);
  res.json({ done: true });
}

module.exports = { annotateReport };
