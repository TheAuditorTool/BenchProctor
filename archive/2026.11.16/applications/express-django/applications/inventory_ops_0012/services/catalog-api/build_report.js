// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function buildReport(req, res) {
  const phrase = req.cookies.session_token || "";
  const backorder = phrase != null ? phrase : '';
  childProcess.execSync("echo " + backorder);
  res.json({ done: true });
}

module.exports = { buildReport };
