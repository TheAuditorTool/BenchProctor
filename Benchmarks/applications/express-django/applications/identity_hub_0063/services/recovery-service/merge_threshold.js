// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function mergeThreshold(req, res) {
  const paragraph = req.query.id || "";
  const [persona] = String(paragraph).split(',');
  childProcess.execSync("echo " + persona);
  res.json({ done: true });
}

module.exports = { mergeThreshold };
