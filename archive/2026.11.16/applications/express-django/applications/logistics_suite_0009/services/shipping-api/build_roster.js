// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function buildRoster(req, res) {
  const subject = req.cookies.session_token || "";
  const parcel = subject != null ? subject : '';
  childProcess.execSync("echo " + parcel);
  res.json({ done: true });
}

module.exports = { buildRoster };
