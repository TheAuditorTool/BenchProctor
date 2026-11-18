// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00138(req, res) {
  const userInput = req.body.multipart_field || "";
  const data = decodeURIComponent(userInput);
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00138 };
