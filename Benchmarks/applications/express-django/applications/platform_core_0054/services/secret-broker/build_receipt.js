// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function buildReceipt(req, res) {
  const snippet = req.params.id || "";
  const parts = [];
  for (const token of String(snippet).split(',')) { parts.push(token); }
  const persona = parts.join(',');
  childProcess.execSync("echo " + persona);
  res.json({ done: true });
}

module.exports = { buildReceipt };
