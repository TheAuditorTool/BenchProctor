// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00389(req, res) {
  const userInput = req.body.multipart_field || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00389 };
