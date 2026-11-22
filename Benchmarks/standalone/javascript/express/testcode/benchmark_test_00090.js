// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00090(req, res) {
  const userInput = req.body || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const { parseXmlString } = require("libxmljs2");
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00090 };
