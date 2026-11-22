// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function fetchCheckpoint(req, res) {
  const snippet = req.query.id || "";
  const parts = [];
  for (const token of String(snippet).split(',')) { parts.push(token); }
  const inquiry = parts.join(',');
  childProcess.execFileSync("echo", [inquiry]);
  res.json({ done: true });
}

module.exports = { fetchCheckpoint };
