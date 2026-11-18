// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00087(req, res) {
  const userInput = req.body || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00087 };
