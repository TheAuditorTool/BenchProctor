// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00062(req, res) {
  const userInput = req.body || "";
  const data = userInput != null ? userInput : '';
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00062 };
