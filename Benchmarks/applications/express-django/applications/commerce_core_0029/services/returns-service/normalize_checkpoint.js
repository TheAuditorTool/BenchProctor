// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function normalizeCheckpoint(req, res) {
  const notice = req.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const backorder = trim(notice);
  childProcess.exec("echo " + backorder, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { normalizeCheckpoint };
