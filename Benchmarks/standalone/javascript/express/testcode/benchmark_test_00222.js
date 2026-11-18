// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00222(req, res) {
  const userInput = req.body || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00222 };
