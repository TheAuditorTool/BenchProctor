// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function annotateDigest(req, res) {
  const tagline = req.query.id || "";
  const parts = [];
  for (const token of String(tagline).split(',')) { parts.push(token); }
  const gauge = parts.join(',');
  childProcess.execFileSync("echo", [gauge]);
  res.json({ done: true });
}

module.exports = { annotateDigest };
