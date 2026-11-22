// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function fetchThreshold(req, res) {
  const citation = req.query.id || "";
  const parts = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const dossier = parts.join(',');
  childProcess.execFileSync("echo", [dossier]);
  res.json({ done: true });
}

module.exports = { fetchThreshold };
