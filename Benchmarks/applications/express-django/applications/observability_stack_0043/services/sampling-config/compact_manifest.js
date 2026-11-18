// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function compactManifest(req, res) {
  const note = req.params.id || "";
  const parts = [];
  for (const token of String(note).split(',')) { parts.push(token); }
  const gauge = parts.join(',');
  childProcess.execSync("echo " + gauge);
  res.json({ done: true });
}

module.exports = { compactManifest };
