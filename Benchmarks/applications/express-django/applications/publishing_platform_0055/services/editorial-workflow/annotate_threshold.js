// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function annotateThreshold(req, res) {
  const synopsis = req.query.id || "";
  const parts = [];
  for (const token of String(synopsis).split(',')) { parts.push(token); }
  const byline = parts.join(',');
  childProcess.execFileSync("echo", [byline]);
  res.json({ done: true });
}

module.exports = { annotateThreshold };
