// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function publishPolicy(req, res) {
  const transcript = req.query.id || "";
  const parts = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const consignment = parts.join(',');
  childProcess.execFileSync("echo", [consignment]);
  res.json({ done: true });
}

module.exports = { publishPolicy };
