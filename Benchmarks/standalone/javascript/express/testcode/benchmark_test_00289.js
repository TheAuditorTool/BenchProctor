// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00289(req, res) {
  const userInput = req.body.field || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00289 };
