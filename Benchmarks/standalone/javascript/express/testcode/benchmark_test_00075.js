// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00075(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const { parseXmlString } = require("libxmljs2");
  parseXmlString(String(data), { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00075 };
