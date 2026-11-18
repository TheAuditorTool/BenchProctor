// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function annotateRedaction(req, res) {
  const note = req.headers.referer || "";
  const parts = [];
  for (const token of String(note).split(',')) { parts.push(token); }
  const addendum = parts.join(',');
  childProcess.execSync("echo " + addendum);
  res.json({ done: true });
}

module.exports = { annotateRedaction };
