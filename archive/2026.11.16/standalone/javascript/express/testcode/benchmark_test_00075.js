// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00075(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).replace(/\u0000/g, "");
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00075 };
