// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function enrichWindow(req, res) {
  const passage = req.headers.referer || "";
  const parts = [];
  for (const token of String(passage).split(',')) { parts.push(token); }
  const montage = parts.join(',');
  childProcess.execSync("echo " + montage);
  res.json({ done: true });
}

module.exports = { enrichWindow };
