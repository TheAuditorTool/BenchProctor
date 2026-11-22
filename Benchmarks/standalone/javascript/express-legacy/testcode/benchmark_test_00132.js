// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00132(req, res) {
  const userInput = req.body || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00132 };
