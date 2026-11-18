// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00209(req, res) {
  const userInput = req.body.payload || "";
  libxmljs.parseXml(userInput, { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00209 };
