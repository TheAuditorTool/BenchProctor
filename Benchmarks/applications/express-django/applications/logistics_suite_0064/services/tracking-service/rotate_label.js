// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function rotateLabel(req, res) {
  const transcript = req.params.id || "";
  const parts = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const parcel = parts.join(',');
  childProcess.execSync("echo " + parcel);
  res.json({ done: true });
}

module.exports = { rotateLabel };
