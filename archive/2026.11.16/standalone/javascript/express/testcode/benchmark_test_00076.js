// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00076(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00076 };
