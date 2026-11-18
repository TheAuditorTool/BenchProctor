// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function publishEscalation(req, res) {
  const phrase = req.body || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const inquiry = normalize(phrase);
  net.connect(80, new URL(String(inquiry)).hostname);
  res.json({ done: true });
}

module.exports = { publishEscalation };
