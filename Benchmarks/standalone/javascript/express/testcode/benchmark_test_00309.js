// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00309(req, res) {
  const userInput = req.body || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00309 };
