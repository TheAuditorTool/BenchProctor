// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function collectRecord(req, res) {
  const citation = req.query.id || "";
  const parts = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const rendition = parts.join(',');
  childProcess.execFileSync("echo", [rendition]);
  res.json({ done: true });
}

module.exports = { collectRecord };
