// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function pruneReceipt(req, res) {
  const phrase = req.headers.authorization || "";
  const [grievance] = String(phrase).split(',');
  childProcess.execSync("echo " + grievance);
  res.json({ done: true });
}

module.exports = { pruneReceipt };
