// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function rotateCheckpoint(req, res) {
  const headline = req.query.id || "";
  const [cohort] = String(headline).split(',');
  childProcess.execSync("echo " + cohort);
  res.json({ done: true });
}

module.exports = { rotateCheckpoint };
