// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function auditReport(req, res) {
  const footnote = req.headers.referer || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const remittance = normalize(footnote);
  childProcess.exec("echo " + remittance, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { auditReport };
