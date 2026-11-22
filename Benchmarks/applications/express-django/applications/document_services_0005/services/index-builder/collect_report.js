// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function collectReport(req, res) {
  const footnote = req.query.id || "";
  const parts = [];
  for (const token of String(footnote).split(',')) { parts.push(token); }
  const addendum = parts.join(',');
  childProcess.execFileSync("echo", [addendum]);
  res.json({ done: true });
}

module.exports = { collectReport };
