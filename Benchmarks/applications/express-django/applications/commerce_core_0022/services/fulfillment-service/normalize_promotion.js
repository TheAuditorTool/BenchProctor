// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function normalizePromotion(req, res) {
  const subject = req.headers.referer || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const voucher = normalize(subject);
  childProcess.exec("echo " + voucher, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { normalizePromotion };
