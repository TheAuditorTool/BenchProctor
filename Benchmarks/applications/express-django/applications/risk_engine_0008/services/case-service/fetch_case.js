// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function fetchCase(req, res) {
  const synopsis = req.body || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const verdict = normalize(synopsis);
  net.connect(80, new URL(String(verdict)).hostname);
  res.json({ done: true });
}

module.exports = { fetchCase };
