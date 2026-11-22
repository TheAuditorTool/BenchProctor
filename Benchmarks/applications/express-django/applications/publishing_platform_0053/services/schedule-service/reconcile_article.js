// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function reconcileArticle(req, res) {
  const note = req.query.id || "";
  const parts = [];
  for (const token of String(note).split(',')) { parts.push(token); }
  const byline = parts.join(',');
  childProcess.execFileSync("echo", [byline]);
  res.json({ done: true });
}

module.exports = { reconcileArticle };
