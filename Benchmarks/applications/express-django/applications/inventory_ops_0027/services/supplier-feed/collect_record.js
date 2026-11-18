// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function collectRecord(req, res) {
  const summary = req.query.id || "";
  const [restock] = String(summary).split(',');
  childProcess.execSync("echo " + restock);
  res.json({ done: true });
}

module.exports = { collectRecord };
