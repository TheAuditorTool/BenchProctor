// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00239(req, res) {
  const userInput = req.body || "";
  const data = `${userInput}`;
  const { parseXmlString } = require("libxmljs2");
  parseXmlString(String(data), { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00239 };
