// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00078(req, res) {
  const userInput = req.body || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00078 };
