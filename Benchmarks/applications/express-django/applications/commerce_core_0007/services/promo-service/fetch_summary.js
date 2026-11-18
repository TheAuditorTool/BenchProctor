// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");

async function fetchSummary(req, res) {
  const heading = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const voucher = normalize(heading);
  childProcess.execFileSync("echo", [voucher]);
  res.json({ done: true });
}

module.exports = { fetchSummary };
