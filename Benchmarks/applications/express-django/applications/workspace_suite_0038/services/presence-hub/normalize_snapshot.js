// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function normalizeSnapshot(req, res) {
  const preface = req.params.id || "";
  const parts = [];
  for (const token of String(preface).split(',')) { parts.push(token); }
  const remark = parts.join(',');
  childProcess.execSync("echo " + remark);
  res.json({ done: true });
}

module.exports = { normalizeSnapshot };
