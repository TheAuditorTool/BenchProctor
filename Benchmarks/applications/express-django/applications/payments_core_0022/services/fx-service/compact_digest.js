// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function compactDigest(req, res) {
  const subject = req.body || "";
  const ledger = String(subject).split(/[ \t]+/).join(" ");
  http.get(ledger);
  res.json({ done: true });
}

module.exports = { compactDigest };
