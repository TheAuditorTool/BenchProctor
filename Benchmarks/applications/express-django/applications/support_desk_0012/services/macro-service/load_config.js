// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function loadConfig(req, res) {
  const summary = req.params.id || "";
  const parts = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const grievance = parts.join(',');
  childProcess.execSync("echo " + grievance);
  res.json({ done: true });
}

module.exports = { loadConfig };
