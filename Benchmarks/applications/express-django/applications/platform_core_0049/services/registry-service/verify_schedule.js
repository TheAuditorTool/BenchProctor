// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function verifySchedule(req, res) {
  const notice = req.params.id || "";
  const trim = (v) => String(v).trim();
  const persona = trim(notice);
  childProcess.execSync("echo " + persona);
  res.json({ done: true });
}

module.exports = { verifySchedule };
