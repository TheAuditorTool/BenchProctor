// SPDX-License-Identifier: Apache-2.0
const libxmljs = require("libxmljs");

async function BenchmarkTest00238(req, res) {
  const userInput = req.body.field || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00238 };
