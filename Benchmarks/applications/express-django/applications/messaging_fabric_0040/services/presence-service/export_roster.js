// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function exportRoster(req, res) {
  const preface = req.body || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const bulletin = normalize(preface);
  net.connect(80, new URL(String(bulletin)).hostname);
  res.json({ done: true });
}

module.exports = { exportRoster };
