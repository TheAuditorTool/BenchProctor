// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");
const libxmljs = require("libxmljs");

async function BenchmarkTest00431(req, res) {
  const userInput = req.body || "";
  const data = nodeUtil.format("%s", userInput);
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00431 };
