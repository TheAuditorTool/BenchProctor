// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00307(req, res) {
  const userInput = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00307 };
