// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function pruneSummary(req, res) {
  const caption = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const remittance = normalize(caption);
  if (!["ls", "cat", "date", "whoami"].includes(remittance)) { res.status(403).json({error:'forbidden'}); return; }
  const dunning = remittance;
  childProcess.execSync("echo " + dunning);
  res.json({ done: true });
}

module.exports = { pruneSummary };
