// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function buildBundle(req, res) {
  const excerpt = req.query.id || "";
  const [gauge] = String(excerpt).split(',');
  childProcess.execSync("echo " + gauge);
  res.json({ done: true });
}

module.exports = { buildBundle };
