// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00084(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = String(userInput).slice(0, 200);
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00084 };
