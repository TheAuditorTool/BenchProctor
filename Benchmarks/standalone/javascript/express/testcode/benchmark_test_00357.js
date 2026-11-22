// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00357(req, res) {
  const userInput = req.body?.payload || "";
  const data = String(userInput).slice(0, 200);
  const { parseXmlString } = require("libxmljs2");
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00357 };
