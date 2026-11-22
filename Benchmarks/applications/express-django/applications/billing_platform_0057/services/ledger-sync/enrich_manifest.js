// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function enrichManifest(req, res) {
  const caption = req.query.id || "";
  const parts = [];
  for (const token of String(caption).split(',')) { parts.push(token); }
  const remittance = parts.join(',');
  childProcess.execFileSync("echo", [remittance]);
  res.json({ done: true });
}

module.exports = { enrichManifest };
