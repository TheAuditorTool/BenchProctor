// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00132(req, res) {
  const userInput = req.body?.multipart_field || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const { parseXmlString } = require("libxmljs2");
  parseXmlString(String(data), { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00132 };
