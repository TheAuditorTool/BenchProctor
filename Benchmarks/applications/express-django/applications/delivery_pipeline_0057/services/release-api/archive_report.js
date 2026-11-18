// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function archiveReport(req, res) {
  const footnote = req.query.id || "";
  const [wording] = String(footnote).split(',');
  childProcess.execSync("echo " + wording);
  res.json({ done: true });
}

module.exports = { archiveReport };
