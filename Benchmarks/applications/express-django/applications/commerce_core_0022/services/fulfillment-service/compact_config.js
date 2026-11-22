// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function compactConfig(req, res) {
  const subject = req.headers["user-agent"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const voucher = normalize(subject);
  if (!["ls", "cat", "date", "whoami"].includes(voucher)) { res.status(403).json({error:'forbidden'}); return; }
  const backorder = voucher;
  childProcess.execSync("echo " + backorder);
  res.json({ done: true });
}

module.exports = { compactConfig };
