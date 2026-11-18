// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function rotateBundle(req, res) {
  const caption = req.params.id || "";
  const parts = [];
  for (const token of String(caption).split(',')) { parts.push(token); }
  const cohort = parts.join(',');
  childProcess.execSync("echo " + cohort);
  res.json({ done: true });
}

module.exports = { rotateBundle };
