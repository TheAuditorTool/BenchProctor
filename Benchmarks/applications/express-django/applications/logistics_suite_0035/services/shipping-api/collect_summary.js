// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function collectSummary(req, res) {
  const phrase = req.body || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const parcel = normalize(phrase);
  net.connect(80, new URL(String(parcel)).hostname);
  res.json({ done: true });
}

module.exports = { collectSummary };
