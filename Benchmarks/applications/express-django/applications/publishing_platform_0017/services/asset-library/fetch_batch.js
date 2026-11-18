// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function fetchBatch(req, res) {
  const summary = req.params.id || "";
  const parts = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const addendum = parts.join(',');
  childProcess.execSync("echo " + addendum);
  res.json({ done: true });
}

module.exports = { fetchBatch };
