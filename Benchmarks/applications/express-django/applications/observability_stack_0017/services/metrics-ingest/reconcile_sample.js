// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function reconcileSample(req, res) {
  const note = req.headers.authorization || "";
  const [cohort] = String(note).split(',');
  childProcess.execSync("echo " + cohort);
  res.json({ done: true });
}

module.exports = { reconcileSample };
