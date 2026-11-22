// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function validateLedger(req, res) {
  const remark = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(remark);
  if (!["ls", "cat", "date", "whoami"].includes(persona)) { res.status(403).json({error:'forbidden'}); return; }
  const notice = persona;
  childProcess.execSync("echo " + notice);
  res.json({ done: true });
}

module.exports = { validateLedger };
