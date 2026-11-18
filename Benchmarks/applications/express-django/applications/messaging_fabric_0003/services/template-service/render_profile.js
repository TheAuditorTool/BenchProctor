// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function renderProfile(req, res) {
  const subject = req.params.id || "";
  const parts = [];
  for (const token of String(subject).split(',')) { parts.push(token); }
  const bulletin = parts.join(',');
  childProcess.execSync("echo " + bulletin);
  res.json({ done: true });
}

module.exports = { renderProfile };
