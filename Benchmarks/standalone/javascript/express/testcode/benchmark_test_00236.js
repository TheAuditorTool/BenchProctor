// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00236(req, res) {
  const userInput = req.body?.field || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00236 };
