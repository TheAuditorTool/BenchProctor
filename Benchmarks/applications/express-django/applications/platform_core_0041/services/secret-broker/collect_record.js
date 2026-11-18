// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function collectRecord(req, res) {
  const passage = req.body || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(passage);
  net.connect(80, new URL(String(persona)).hostname);
  res.json({ done: true });
}

module.exports = { collectRecord };
