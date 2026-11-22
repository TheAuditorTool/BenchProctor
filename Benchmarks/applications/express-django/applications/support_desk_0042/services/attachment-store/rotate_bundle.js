// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function rotateBundle(req, res) {
  const blurb = req.headers.authorization || "";
  const [inquiry] = String(blurb).split(',');
  childProcess.execSync("echo " + inquiry);
  res.json({ done: true });
}

module.exports = { rotateBundle };
